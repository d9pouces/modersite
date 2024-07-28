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
DF_SITE_SOCIAL_NETWORKS = {
    "instagram": "https://www.instagram.com/d9pouces/",
    "twitter": "https://x.com/d9pouces/",
    "github": "https://github.com/d9pouces/",
}
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
CSP_REPORT_URI = "/csp-report/"
CSP_REPORT_TO = None

DF_TEMPLATE_CONTEXT_PROCESSORS = [
    "modersite.context_processors.global_site_infos",
    "django.template.context_processors.request",
]
DF_INSTALLED_APPS = [
    "django_bootstrap5",
    "modersite.app.ModersiteApp",
    "cookie_consent",
    "postman",
    "allauth.mfa",
    "allauth.usersessions",
    "django_ckeditor_5",
]
DF_MIDDLEWARE = [
    "allauth.usersessions.middleware.UserSessionsMiddleware",
    "df_websockets.middleware.WebsocketMiddleware",
    "modersite.middleware.websocket_middleware",
]
MIDDLEWARE = [
    "django.middleware.cache.UpdateCacheMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "df_config.apps.middleware.DFConfigMiddleware",
    "allauth.usersessions.middleware.UserSessionsMiddleware",
    "df_websockets.middleware.WebsocketMiddleware",
    "modersite.middleware.websocket_middleware",
    "csp.middleware.CSPMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",
]
USERSESSIONS_TRACK_ACTIVITY = True
POSTMAN_DISALLOW_ANONYMOUS = True
POSTMAN_AUTO_MODERATE_AS = True
POSTMAN_I18N_URLS = False
AUTH_USER_MODEL = "modersite.PreferencesUser"
COOKIE_CONSENT_SECURE = SettingReference("USE_SSL")
COOKIE_CONSENT_DOMAIN = "{SERVER_NAME}"
COOKIE_CONSENT_SAMESITE = "Strict"

PIPELINE = {
    "PIPELINE_ENABLED": SettingReference("PIPELINE_ENABLED"),
    "JAVASCRIPT": {
        "base": {
            "source_filenames": [
                "js/base.js",
                "js/df_websockets.min.js",
                # "django_ckeditor_5/dist/bundle.js"
            ],
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
            "source_filenames": [
                "django_ckeditor_5/src/override-django.css",
                "css/ckeditor5.css",
                "css/base.css",
            ],
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
SOCIALACCOUNT_EMAIL_AUTHENTICATION_AUTO_CONNECT = True
SOCIALACCOUNT_LOGIN_ON_GET = True

CKEDITOR_5_USER_LANGUAGE = True
special_chars = [
    {"title": _("smiley face"), "character": "😊"},
    {"title": _("smiley face"), "character": ":)"},
]
CK_EDITOR_5_UPLOAD_FILE_VIEW = "django_ckeditor_5.views.upload_file"
CK_EDITOR_5_UPLOAD_FILE_VIEW_NAME = "upload_file"
CKEDITOR_5_CONFIGS = {
    "inline": {
        "specialChars": special_chars,
        "toolbar": [
            "bold",
            "italic",
            "underline",
            "strikethrough",
            "subscript",
            "superscript",
            "|",
            "specialCharacters",
            "removeFormat",
        ],
        "plugins": [
            "Essentials",
            "Autoformat",
            "Bold",
            "Italic",
            "Underline",
            "Strikethrough",
            "Code",
            "Subscript",
            "Superscript",
            "Paragraph",
            "Font",
            "PasteFromOffice",
            "RemoveFormat",
            "Highlight",
            "SpecialCharacters",
            "SpecialCharactersEssentials",
            "ShowBlocks",
            "SelectAll",
        ],
    },
    "inline_link": {
        "specialChars": special_chars,
        "toolbar": [
            "bold",
            "italic",
            "underline",
            "strikethrough",
            "subscript",
            "superscript",
            "link",
            "|",
            "specialCharacters",
            "removeFormat",
        ],
        "plugins": [
            "Essentials",
            "Autoformat",
            "Bold",
            "Italic",
            "Underline",
            "Strikethrough",
            "Code",
            "Subscript",
            "Superscript",
            "Link",
            "Paragraph",
            "Font",
            "PasteFromOffice",
            "RemoveFormat",
            "Highlight",
            "SpecialCharacters",
            "SpecialCharactersEssentials",
            "ShowBlocks",
            "SelectAll",
        ],
    },
    "default": {
        "specialChars": special_chars,
        "toolbar": [
            "heading",
            "bulletedList",
            "numberedList",
            "blockQuote",
            "|",
            "bold",
            "italic",
            "underline",
            "strikethrough",
            "subscript",
            "superscript",
            "link",
            "highlight",
            "|",
            "insertTable",
            "insertImage",
            "specialCharacters",
            "removeFormat",
            "undo",
            "redo",
        ],
        "image": {
            "toolbar": [
                "imageTextAlternative",
                "|",
                "imageStyle:full",
                "imageStyle:alignLeft",
                "imageStyle:alignRight",
                "imageStyle:alignCenter",
                "imageStyle:side",
                "|",
            ],
            "styles": [
                "full",
                "side",
                "alignLeft",
                "alignRight",
                "alignCenter",
            ],
        },
        "list": {"properties": {"styles": False, "startIndex": True, "reversed": True}},
        "table": {
            "defaultHeadings": {"rows": 1, "columns": 1},
            "contentToolbar": ["tableColumn", "tableRow", "mergeTableCells"],
        },
    },
}
