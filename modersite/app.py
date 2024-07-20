"""Configuration for the modersite app."""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ModersiteApp(AppConfig):
    """Configuration for the modersite app."""

    default_auto_field = "django.db.models.AutoField"
    name = "modersite"
    verbose_name = _("ModerSite")

    def ready(self):
        """Run code when the app is ready."""
        super().ready()
        from django.conf import settings
        from django.contrib.sites.models import Site

        site, created = Site.objects.get_or_create(
            id=1,
            defaults={
                "domain": settings.SERVER_NAME,
                "name": settings.DF_SITE_TITLE,
            },
        )
        site.domain = settings.SERVER_NAME
        site.name = settings.DF_SITE_TITLE
        site.save()
