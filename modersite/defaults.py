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
    "modersite.app.ModersiteApp",
    "django_bootstrap5",
    "cookie_consent",
    "postman",
    "allauth.mfa",
    "allauth.usersessions",
    "django_ckeditor_5",
]
DF_MIDDLEWARE = [
    "allauth.usersessions.middleware.UserSessionsMiddleware",
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
            "source_filenames": ["js/base.js", "js/df_websockets.min.js", "django_ckeditor_5/dist/bundle.js"],
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
                "css/base.css",
                "django_ckeditor_5/dist/styles.css",
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

CKEDITOR_5_CONFIGS = {
    "default": {
        "toolbar": [
            "heading",
            "|",
            "bold",
            "italic",
            "link",
            "bulletedList",
            "numberedList",
            "blockQuote",
            "imageUpload",
        ],
    },
    "comment2": {
        "toolbar": [
            "heading",
            "|",
            "bold",
            "italic",
            "link",
            "bulletedList",
            "numberedList",
            "blockQuote",
            "imageUpload",
        ],
    },
    "extends": {
        "blockToolbar": [
            "paragraph",
            "heading1",
            "heading2",
            "heading3",
            "|",
            "bulletedList",
            "numberedList",
            "|",
            "blockQuote",
        ],
        "toolbar": [
            "heading",
            "|",
            "outdent",
            "indent",
            "|",
            "bold",
            "italic",
            "link",
            "underline",
            "strikethrough",
            "code",
            "subscript",
            "superscript",
            "highlight",
            "|",
            "codeBlock",
            "sourceEditing",
            "insertImage",
            "bulletedList",
            "numberedList",
            "todoList",
            "|",
            "blockQuote",
            "imageUpload",
            "|",
            "fontSize",
            "fontFamily",
            "fontColor",
            "fontBackgroundColor",
            "mediaEmbed",
            "removeFormat",
            "insertTable",
        ],
        "image": {
            "toolbar": [
                "imageTextAlternative",
                "|",
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
        "table": {
            "contentToolbar": ["tableColumn", "tableRow", "mergeTableCells", "tableProperties", "tableCellProperties"],
        },
        "heading": {
            "options": [
                {"model": "paragraph", "title": "Paragraph", "class": "ck-heading_paragraph"},
                {"model": "heading1", "view": "h1", "title": "Heading 1", "class": "ck-heading_heading1"},
                {"model": "heading2", "view": "h2", "title": "Heading 2", "class": "ck-heading_heading2"},
                {"model": "heading3", "view": "h3", "title": "Heading 3", "class": "ck-heading_heading3"},
            ]
        },
    },
    "list": {
        "properties": {
            "styles": "true",
            "startIndex": "true",
            "reversed": "true",
        }
    },
}
