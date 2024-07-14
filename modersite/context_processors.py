"""Define the context processors with global variables about the site."""

import logging
from typing import Any, Dict

from django.conf import settings
from django.http import HttpRequest

from modersite.user_settings import get_user_setting

logger = logging.getLogger(__name__)


def global_site_infos(request: HttpRequest) -> Dict[str, Any]:
    """Adds a few values to the request context."""
    try:
        color_theme = get_user_setting("color_theme", request=request)
    except Exception as e:
        logger.error("Error getting color theme: %s", e)
    return {
        "DF_SITE_TITLE": settings.DF_SITE_TITLE,
        "DF_SITE_DESCRIPTION": settings.DF_SITE_DESCRIPTION,
        "DF_SITE_KEYWORDS": settings.DF_SITE_KEYWORDS,
        "DF_SITE_AUTHOR": settings.DF_SITE_AUTHOR,
        "DF_SITE_ORGANIZATION": settings.DF_SITE_ORGANIZATION,
        "DF_SITE_X_ACCOUNT": settings.DF_SITE_X_ACCOUNT,
        "DF_COLOR_THEMES": settings.DF_SITE_THEMES,
        "DF_MICROSOFT_BACKGROUND_COLOR": settings.DF_MICROSOFT_BACKGROUND_COLOR,
        "COLOR_THEME": color_theme,
    }
