"""List of URLs for the modersite app."""

from django.urls import path

from modersite.views import BrowserConfigView, DemoView, site_webmanifest_view, theme_switch

urlpatterns = [
    path("site.webmanifest", site_webmanifest_view, name="site_webmanifest"),
    path("browserconfig.xml", BrowserConfigView.as_view(), name="browserconfig"),
    path("df/theme-switch", theme_switch, name="theme_switch"),
    path("demo/", DemoView.as_view(), name="demo"),
]