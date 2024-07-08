"""Define the context processors with global variables about the site."""

from django.conf import settings


def global_site_infos(request):
    """Adds a few values to the request context."""
    return {
        "DF_SITE_TITLE": settings.DF_SITE_TITLE,
        "DF_SITE_DESCRIPTION": settings.DF_SITE_DESCRIPTION,
        "DF_SITE_KEYWORDS": settings.DF_SITE_KEYWORDS,
        "DF_SITE_AUTHOR": settings.DF_SITE_AUTHOR,
        "DF_SITE_ORGANIZATION": settings.DF_SITE_ORGANIZATION,
        "DF_SITE_X_ACCOUNT": settings.DF_SITE_X_ACCOUNT,
        "DF_MICROSOFT_BACKGROUND_COLOR": settings.DF_MICROSOFT_BACKGROUND_COLOR,
    }
