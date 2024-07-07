"""Views for the modersite app."""

from df_websockets.tasks import set_websocket_topics
from django.views.generic import TemplateView


class IndexView(TemplateView):
    """Default index view."""

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        """Get the context data for the view."""
        context = super().get_context_data(**kwargs)
        set_websocket_topics(self.request)
        return context
