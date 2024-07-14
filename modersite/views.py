"""Views for the modersite app."""

import logging

from df_websockets.tasks import set_websocket_topics
from django.conf import settings
from django.contrib import messages
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.templatetags.static import static
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme, urlencode
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView

from modersite.user_settings import set_user_setting

logger = logging.getLogger(__name__)


def site_webmanifest_view(request: HttpRequest) -> HttpResponse:
    """Generate a site.webmanifest view."""
    result = {
        "name": settings.DF_SITE_TITLE,
        "short_name": settings.DF_SITE_TITLE,
        "icons": [
            {"src": static("favicon/android-chrome-1192x192.png"), "sizes": "192x192", "type": "image/png"},
            {"src": static("favicon/android-chrome-512x512.png"), "sizes": "512x512", "type": "image/png"},
        ],
        "theme_color": settings.DF_ANDROID_THEME_COLOR,
        "background_color": settings.DF_ANDROID_BACKGROUND_COLOR,
        "display": "standalone",
    }

    return JsonResponse(result)


class BrowserConfigView(TemplateView):
    """View for the browserconfig.xml file."""

    template_name = "favicon/browserconfig.xml"
    content_type = "application/xml"


class IndexView(TemplateView):
    """Default index view."""

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        """Get the context data for the view."""
        context = super().get_context_data(**kwargs)
        set_websocket_topics(self.request)
        return context


@never_cache
def theme_switch(request: HttpRequest) -> HttpResponse:
    """Change the color theme of the site."""
    current_theme: str = request.GET.get("current", "auto")
    redirect_to: str = request.GET.get("next", "/")
    if not url_has_allowed_host_and_scheme(
        url=redirect_to,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    ):
        redirect_to = "/"

    if settings.DF_SITE_THEMES:
        next_theme, __, next_icon = settings.DF_SITE_THEMES[-1]
        for theme, label, icon in settings.DF_SITE_THEMES:
            if theme == current_theme:
                break
            next_theme, next_icon = theme, icon
    else:
        next_theme, next_icon = "auto", "toggle-on"
    next_url = reverse("theme_switch")
    args = urlencode({"next": redirect_to, "current": next_theme})
    result = {"theme": next_theme, "icon": next_icon, "href": f"{next_url}?{args}"}
    if request.META["HTTP_ACCEPT"] == "application/json":
        response = JsonResponse(result)
    else:
        response = HttpResponseRedirect(redirect_to)
    set_user_setting("color_theme", next_theme, request=request, response=response)
    return response


class DemoView(TemplateView):
    """Demo view with many Bootstrap functionnalities."""

    template_name = "demo.html"

    def get_context_data(self, **kwargs):
        """Get the context data for the view."""
        context = super().get_context_data(**kwargs)
        set_websocket_topics(self.request)
        messages.error(self.request, "This is an error message.")
        return context
