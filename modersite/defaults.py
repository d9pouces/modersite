"""Django settings for the project."""

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
