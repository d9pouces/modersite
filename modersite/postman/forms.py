"""Forms for the Postman application."""

from django import forms
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.widgets import CKEditor5Widget
from postman.forms import AnonymousWriteForm, FullReplyForm, QuickReplyForm, WriteForm


class HTMLWriteForm(WriteForm):
    """Form used by authenticated users."""

    body = forms.CharField(
        widget=CKEditor5Widget(attrs={"class": "django_ckeditor_5"}, config_name="postman"), label=_("body")
    )


class HTMLAnonymousWriteForm(AnonymousWriteForm):
    """Form used by anonymous users."""

    body = forms.CharField(
        widget=CKEditor5Widget(attrs={"class": "django_ckeditor_5"}, config_name="postman"), label=_("body")
    )


class HTMLFullReplyForm(FullReplyForm):
    """Form for complete Postman replies."""

    body = forms.CharField(
        widget=CKEditor5Widget(attrs={"class": "django_ckeditor_5"}, config_name="postman"), label=_("body")
    )


class HTMLQuickReplyForm(QuickReplyForm):
    """Form for postman quick replies."""

    body = forms.CharField(
        widget=CKEditor5Widget(attrs={"class": "django_ckeditor_5"}, config_name="postman"), label=_("body")
    )
