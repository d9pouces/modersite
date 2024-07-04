"""Views for the modersite app."""

from django.views.generic import TemplateView


class IndexView(TemplateView):
    """Default index view."""

    template_name = "index.html"
