"""Views for the modersite app."""

from df_websockets.tasks import set_websocket_topics
from django.conf import settings
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.templatetags.static import static
from django.views.generic import TemplateView


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
