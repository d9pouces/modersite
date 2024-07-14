"""Models for the modersite app."""

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from modersite.defaults import DF_SITE_THEMES


class AbstractPreferences(models.Model):
    """User preferences for the modersite app."""

    COLOR_THEMES = {x[0]: x[1] for x in DF_SITE_THEMES}
    color_theme = models.CharField(
        max_length=10,
        default=DF_SITE_THEMES[0][0],
        db_index=True,
        choices=COLOR_THEMES,
        verbose_name=_("Color theme"),
    )
    display_online = models.BooleanField(default=False, verbose_name=_("Display online status"), db_index=True)

    class Meta:
        """Meta options for the model."""

        abstract = True


class PreferencesUser(AbstractUser, AbstractPreferences):
    """User model for the modersite app."""

    def __str__(self):
        """Return the string representation of the user."""
        return super().__str__()
