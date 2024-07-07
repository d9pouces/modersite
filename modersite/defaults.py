"""Django settings for the project."""

from df_config.config.dynamic_settings import SettingReference

DF_INDEX_VIEW = "modersite.views.IndexView"
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
            "integrity": "sha384",
            "crossorigin": "anonymous",
            "extra_context": {
                "defer": True,
            },
        },
        "app": {
            "source_filenames": ["js/app.ts"],
            "output_filename": "js/app.min.js",
            "integrity": "sha384",
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
        },
    },
    "CSS_COMPRESSOR": "pipeline.compressors.yuglify.YuglifyCompressor",
    "JS_COMPRESSOR": "pipeline.compressors.uglifyjs.UglifyJSCompressor",
    "COMPILERS": [],
}
