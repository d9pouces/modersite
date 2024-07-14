"""Configuration for the modersite app."""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ModersiteApp(AppConfig):
    """Configuration for the modersite app."""

    default_auto_field = "django.db.models.AutoField"
    name = "modersite"
    verbose_name = _("ModerSite")
