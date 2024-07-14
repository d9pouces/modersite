"""Django settings for the project."""

from typing import List, Tuple

from df_config.config.dynamic_settings import SettingReference
from django.utils.translation import gettext_lazy as _

DF_INDEX_VIEW = "modersite.views.IndexView"
DF_SITE_TITLE = "Technological proof of concept"
DF_SITE_DESCRIPTION = "This is a technological proof of concept."
DF_SITE_KEYWORDS = ["Django", "Bootstrap", "WebSockets", "HTMX", "Django Channels"]
DF_SITE_AUTHOR = "d9pouces"
DF_SITE_ORGANIZATION = "d9pouces"
DF_SITE_X_ACCOUNT = "d9pouces"
DF_SITE_THEMES: List[Tuple[str, str, str]] = [  # ('theme name', 'theme label', 'icon name')
    ("auto", _("Auto"), "toggle-on"),
    ("light", _("Light"), "sun"),
    ("dark", _("Dark"), "moon"),
]
DF_ANDROID_THEME_COLOR = "#ffffff"
DF_ANDROID_BACKGROUND_COLOR = "#ffffff"
DF_MICROSOFT_BACKGROUND_COLOR = "#da532c"
CSP_IMG_SRC = ["'self'", "data: w3.org/svg/2000"]
CSP_STYLE_SRC = [
    "'self'",
    "https://fonts.googleapis.com",
]
CSP_FONT_SRC = ["'self'", "https://fonts.gstatic.com"]
CSP_DEFAULT_SRC = ["'none'"]
CSP_SCRIPT_SRC = ["'self'"]
CSP_OBJECT_SRC = ["'self'"]
CSP_MEDIA_SRC = ["'self'"]
CSP_FRAME_SRC = ["'self'"]
CSP_CHILD_SRC = ["'self'"]
CSP_FRAME_ANCESTORS = ["'self'"]
CSP_FORM_ACTION = ["'self'"]
CSP_MANIFEST_SRC = ["'self'"]
CSP_BASE_URI = ["'self'"]
DF_TEMPLATE_CONTEXT_PROCESSORS = [
    "modersite.context_processors.global_site_infos",
]
DF_INSTALLED_APPS = ["modersite.app.ModersiteApp", "django_bootstrap5"]
AUTH_USER_MODEL = "modersite.PreferencesUser"

DF_JS = [
    "js/main.js",
]
DF_CSS = ["css/theme.css"]
PIPELINE = {
    "PIPELINE_ENABLED": SettingReference("PIPELINE_ENABLED"),
    "JAVASCRIPT": {
        "base": {
            "source_filenames": ["js/base.js", "js/df_websockets.min.js"],
            "output_filename": "js/base.min.js",
            #            "integrity": "sha384",
            "crossorigin": "anonymous",
            "extra_context": {
                "defer": True,
            },
        },
        "app": {
            "source_filenames": ["js/app.ts"],
            "output_filename": "js/app.min.js",
            #            "integrity": "sha384",
            "crossorigin": "anonymous",
            "extra_context": {
                "defer": True,
            },
        },
    },
    "STYLESHEETS": {
        "base": {
            "source_filenames": ["css/base.css"],
            "output_filename": "css/base.min.css",
            "extra_context": {"media": "all"},
            #            "integrity": "sha384",
            "crossorigin": "anonymous",
        },
        "app": {
            "source_filenames": ["css/app.css"],
            "output_filename": "css/app.min.css",
            "extra_context": {"media": "all"},
            #            "integrity": "sha384",
            "crossorigin": "anonymous",
        },
    },
    "CSS_COMPRESSOR": "pipeline.compressors.yuglify.YuglifyCompressor",
    "JS_COMPRESSOR": "pipeline.compressors.uglifyjs.UglifyJSCompressor",
    "COMPILERS": [],
}
