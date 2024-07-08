"""List of URLs for the modersite app."""

from django.urls import path

from modersite.views import BrowserConfigView, site_webmanifest_view

urlpatterns = [
    path("site.webmanifest", site_webmanifest_view, name="site_webmanifest"),
    path("browserconfig.xml", BrowserConfigView.as_view(), name="browserconfig"),
]
