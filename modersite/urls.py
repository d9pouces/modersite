"""List of URLs for the modersite app."""

from django.urls import include, path

from modersite.views import BrowserConfigView, DemoView, PopupDemoView, site_webmanifest_view

urlpatterns = [
    path("site.webmanifest", site_webmanifest_view, name="site_webmanifest"),
    path("browserconfig.xml", BrowserConfigView.as_view(), name="browserconfig"),
    path("users/", include("modersite.users.urls", namespace="users")),
    path("messages/", include("postman.urls", namespace="postman")),
    path("cookies/", include("cookie_consent.urls")),
    path("demo/", DemoView.as_view(), name="demo"),
    path("popup-demo/", PopupDemoView.as_view(), name="popup-demo"),
]
