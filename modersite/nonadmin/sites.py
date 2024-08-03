"""Custom site for the user-facing part of the application."""

from functools import update_wrapper

from django.contrib.admin import AdminSite
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

import settings


class NonAdminSite(AdminSite):
    """Custom site for the user-facing part of the application."""

    site_title = settings.DF_SITE_TITLE
    site_header = settings.DF_SITE_TITLE
    index_title = settings.DF_SITE_TITLE

    def __init__(self, name="modersite"):
        """Create a new instance of the view site.

        Overriding the default AdminSite to use the custom site name.
        """
        super().__init__(name)

    @property
    def site_url(self):
        """Return the URL for the index view."""
        return reverse("index")

    def has_permission(self, request):
        """Always return True. This is a placeholder for the permission system."""
        return True

    def admin_view(self, view, cacheable=False):
        """Decorator to create an admin view attached to this ``AdminSite``.

        This wraps the view and provides permission checking by calling
        ``self.has_permission``.

        You'll want to use this from within ``AdminSite.get_urls()``:

            class MyAdminSite(AdminSite):

                def get_urls(self):
                    from django.urls import path

                    urls = super().get_urls()
                    urls += [
                        path('my_view/', self.admin_view(some_view))
                    ]
                    return urls

        By default, admin_views are marked non-cacheable using the
        ``never_cache`` decorator. If the view can be safely cached, set
        cacheable=True.
        """

        def inner(request, *args, **kwargs):
            if not self.has_permission(request):
                if request.path == reverse("account_logout", current_app=self.name):
                    index_path = reverse("index", current_app=self.name)
                    return HttpResponseRedirect(index_path)
                # Inner import to prevent django.contrib.admin (app) from
                # importing django.contrib.auth.models.User (unrelated model).
                from django.contrib.auth.views import redirect_to_login

                return redirect_to_login(
                    request.get_full_path(),
                    reverse("account_login", current_app=self.name),
                )
            return view(request, *args, **kwargs)

        if not cacheable:
            inner = never_cache(inner)
        # We add csrf_protect here so this function can be used as a utility
        # function for any view, without having to repeat 'csrf_protect'.
        if not getattr(view, "csrf_exempt", False):
            inner = csrf_protect(inner)
        return update_wrapper(inner, view)

    def get_urls(self):
        """Return the URL patterns for the user site."""
        # Since this module gets imported in the application's root package,
        # it cannot import models from other applications at the module level,
        # and django.contrib.contenttypes.views imports ContentType.
        from django.urls import include, path

        def wrap(view, cacheable=False):
            def wrapper(*args, **kwargs):
                return self.admin_view(view, cacheable)(*args, **kwargs)

            wrapper.admin_site = self
            return update_wrapper(wrapper, view)

        # Admin-site-wide views.
        urlpatterns = [
            path("autocomplete/", wrap(self.autocomplete_view), name="autocomplete"),
        ]

        # Add in each model's views
        for model, model_admin in self._registry.items():
            # noinspection PyProtectedMember
            opts = model._meta
            urlpatterns += [
                path(
                    f"{opts.app_label}/{opts.model_name}/",
                    include(model_admin.urls),
                ),
            ]

        return urlpatterns

    @property
    def urls(self):
        """Return the URL patterns for the user site."""
        return self.get_urls(), "views", self.name


site = NonAdminSite()
