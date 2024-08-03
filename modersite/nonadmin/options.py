"""Component that lists items found in a queryset."""

from functools import partial, update_wrapper

from django import forms
from django.contrib.admin import ModelAdmin, helpers
from django.contrib.admin.exceptions import DisallowedModelAdminToField
from django.contrib.admin.options import IS_POPUP_VAR, TO_FIELD_VAR, get_content_type_for_model
from django.contrib.admin.templatetags.admin_urls import add_preserved_filters
from django.contrib.admin.utils import (
    flatten_fieldsets,
    unquote,
)
from django.core.exceptions import (
    FieldError,
    PermissionDenied,
)
from django.forms import modelform_factory
from django.forms.models import modelform_defines_fields
from django.template.response import TemplateResponse
from django.utils.translation import gettext as _


class ModelView(ModelAdmin):
    """ModelAdmin subclass that also provides a readonly view."""

    show_fields = None
    show_fieldsets = None
    view_form_template = None

    def get_urls(self):
        """Return the URL patterns for the model."""
        from django.urls import path

        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)

            wrapper.model_admin = self
            return update_wrapper(wrapper, view)

        app_label = self.opts.app_label
        model_name = self.opts.model_name

        return [
            path("list/", wrap(self.changelist_view), name=f"{app_label}_{model_name}_changelist"),
            path("add/", wrap(self.add_view), name=f"{app_label}_{model_name}_add"),
            path(
                "<path:object_id>/delete/",
                wrap(self.delete_view),
                name=f"{app_label}_{model_name}_delete",
            ),
            path(
                "<path:object_id>/change/",
                wrap(self.change_view),
                name=f"{app_label}_{model_name}_change",
            ),
            path(
                "<path:object_id>/show/",
                wrap(self.change_view),
                name=f"{app_label}_{model_name}_show",
            ),
        ]

    def show_view(self, request, object_id, form_url, extra_context):
        """Display an object."""
        to_field = request.GET.get(TO_FIELD_VAR)
        if to_field and not self.to_field_allowed(request, to_field):
            raise DisallowedModelAdminToField(f"The field {to_field} cannot be referenced.")

        obj = self.get_object(request, unquote(object_id), to_field)

        if not self.has_view_permission(request, obj):
            raise PermissionDenied

        elif obj is None:
            return self._get_obj_does_not_exist_redirect(request, self.opts, object_id)

        fieldsets = self.get_show_fieldsets(request, obj)
        model_form_class = self.get_show_form(request, obj, fields=flatten_fieldsets(fieldsets))
        form = model_form_class(instance=obj)
        formsets, inline_instances = self._create_formsets(request, obj, change=True)

        readonly_fields = flatten_fieldsets(fieldsets)
        admin_form = helpers.AdminForm(
            form,
            list(fieldsets),
            # Clear prepopulated fields on a view-only form to avoid a crash.
            {},
            readonly_fields,
            model_admin=self,
        )
        media = self.media + admin_form.media

        inline_formsets = self.get_inline_formsets(request, formsets, inline_instances, obj)
        for inline_formset in inline_formsets:
            media += inline_formset.media

        title = _("View %s") % self.opts.verbose_name
        context = {
            **self.admin_site.each_context(request),
            "title": title,
            "subtitle": str(obj) if obj else None,
            "adminform": admin_form,
            "object_id": object_id,
            "original": obj,
            "is_popup": IS_POPUP_VAR in request.GET,
            "to_field": to_field,
            "media": media,
            "inline_admin_formsets": inline_formsets,
            "errors": helpers.AdminErrorList(form, formsets),
            "preserved_filters": self.get_preserved_filters(request),
        }
        context.update(extra_context or {})

        return self.render_view_form(request, context, add=False, change=True, obj=obj, form_url=form_url)

    def render_view_form(self, request, context, add=False, change=False, form_url="", obj=None):
        """Render the view form."""
        app_label = self.opts.app_label
        preserved_filters = self.get_preserved_filters(request)
        form_url = add_preserved_filters({"preserved_filters": preserved_filters, "opts": self.opts}, form_url)
        view_on_site_url = self.get_view_on_site_url(obj)
        context.update(
            {
                "add": False,
                "change": False,
                "has_view_permission": self.has_view_permission(request, obj),
                "has_add_permission": self.has_add_permission(request),
                "has_change_permission": self.has_change_permission(request, obj),
                "has_delete_permission": self.has_delete_permission(request, obj),
                "has_editable_inline_admin_formsets": False,
                "has_file_field": False,
                "has_absolute_url": view_on_site_url is not None,
                "absolute_url": view_on_site_url,
                "form_url": form_url,
                "opts": self.opts,
                "content_type_id": get_content_type_for_model(self.model).pk,
                "save_as": False,
                "save_on_top": False,
                "is_popup_var": IS_POPUP_VAR,
                "app_label": app_label,
            }
        )
        request.current_app = self.admin_site.name

        return TemplateResponse(
            request,
            self.view_form_template
            or [
                f"admin/{app_label}/{self.opts.model_name}/view_form.html",
                f"admin/{app_label}/view_form.html",
                "admin/view_form.html",
            ],
            context,
        )

    def get_show_fields(self, request, obj=None):
        """Hook for specifying fields."""
        if self.show_fields:
            return self.show_fields
        # _get_form_for_get_fields() is implemented in subclasses.
        form = self._get_form_for_get_fields(request, obj)
        return [*form.base_fields, *self.get_readonly_fields(request, obj)]

    def get_show_fieldsets(self, request, obj=None):
        """Hook for specifying fieldsets."""
        if self.show_fieldsets:
            return self.show_fieldsets
        return [(None, {"fields": self.get_show_fields(request, obj)})]

    def get_show_form(self, request, obj=None, **kwargs):
        """Return a Form class for use in the admin add view.

        This is used by add_view and change_view.
        """
        if "fields" in kwargs:
            fields = kwargs.pop("fields")
        else:
            fields = flatten_fieldsets(self.get_show_fieldsets(request, obj))
        exclude = fields

        # Remove declared form fields which are in readonly_fields.
        new_attrs = dict.fromkeys(f for f in exclude if f in self.form.declared_fields)
        form = type(self.form.__name__, (self.form,), new_attrs)

        defaults = {
            "form": form,
            "fields": fields,
            "exclude": exclude,
            "formfield_callback": partial(self.formfield_for_dbfield, request=request),
            **kwargs,
        }

        if defaults["fields"] is None and not modelform_defines_fields(defaults["form"]):
            defaults["fields"] = forms.ALL_FIELDS

        try:
            return modelform_factory(self.model, **defaults)
        except FieldError as e:
            raise FieldError(f"{e}. Check fields/fieldsets/exclude attributes of class {self.__class__.__name__}.")
