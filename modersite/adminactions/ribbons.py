"""Show ribbons in the user-facing part."""

from modersite.nonadmin.options import ModelView


class RibbonView(ModelView):
    """ModelView subclass for the ribbon model."""

    list_display = ("message", "color", "start_date", "end_date", "is_active")
    list_filter = ("color", "start_date", "end_date", "is_active")
    search_fields = ("summary",)
