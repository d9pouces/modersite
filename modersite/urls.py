"""List of URLs for the modersite app."""

from django.urls import include, path

import settings
from modersite.views import BrowserConfigView, DemoView, PopupDemoView, csp_report_view, site_webmanifest_view

urlpatterns = [
    path("site.webmanifest", site_webmanifest_view, name="site_webmanifest"),
    path("browserconfig.xml", BrowserConfigView.as_view(), name="browserconfig"),
    path(settings.CSP_REPORT_URI[1:], csp_report_view, name="csp_report"),
    path("users/", include("modersite.users.urls", namespace="users")),
    path("messages/", include("modersite.postman.urls", namespace="postman")),
    path("cookies/", include("cookie_consent.urls")),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
    path("demo/", DemoView.as_view(), name="demo"),
    path("popup-demo/", PopupDemoView.as_view(), name="popup-demo"),
]
