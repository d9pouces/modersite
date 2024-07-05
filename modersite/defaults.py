"""Django settings for the project."""

from df_config.config.dynamic_settings import SettingReference

DF_INDEX_VIEW = "modersite.views.IndexView"
CSP_IMG_SRC = ["'self'", "data: w3.org/svg/2000"]
CSP_STYLE_SRC = [
    "'self'",
    "https://fonts.googleapis.com",
]
CSP_FONT_SRC = ["'self'", "https://fonts.gstatic.com"]
DF_JS = [
    "js/main.js",
]
DF_CSS = ["css/theme.css"]
PIPELINE = {
    "PIPELINE_ENABLED": SettingReference("PIPELINE_ENABLED"),
    "JAVASCRIPT": {
        "default": {
            "source_filenames": ["js/main.js"],
            "output_filename": "js/default.js",
            "integrity": "sha384",
            "crossorigin": "anonymous",
            "extra_context": {
                "defer": True,
            },
        },
    },
    "STYLESHEETS": {
        "default": {
            "source_filenames": ["css/theme.css"],
            "output_filename": "css/default.css",
            "extra_context": {"media": "all"},
        },
    },
    "CSS_COMPRESSOR": "pipeline.compressors.yuglify.YuglifyCompressor",
    "JS_COMPRESSOR": "pipeline.compressors.uglifyjs.UglifyJSCompressor",
    "COMPILERS": [
        "pipeline.compilers.sass.SASSCompiler",
        "df_config.apps.pipeline.TypescriptCompiler",
    ],
}
