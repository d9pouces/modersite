"""Custom form fields for the modersite app."""

import html
from functools import lru_cache
from typing import Dict, Iterable, List, Set

import bleach
from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags
from django_ckeditor_5.widgets import CKEditor5Widget

# list of CKEditor5 plugins and associated HTML tags
BLOCK = "$block"
TAGS_BY_PLUGIN: Dict[str, Dict[str, List[str]]] = {
    "Alignment": {BLOCK: ["class"]},
    "BlockQuote": {"blockquote": []},
    "Bold": {"strong": []},
    "Code": {"code": []},
    "CodeBlock": {"pre": ["class"], "code": ["class"]},
    "Essentials": {"br": []},
    "Font": {"span": ["class"]},
    "Heading": {"h1": [], "h2": [], "h3": [], "h4": []},
    "Highlight": {"mark": ["class"]},
    "HorizontalLine": {"hr": []},
    "HtmlEmbed": {"div": ["class"]},
    "Image": {"figure": ["class"], "img": []},
    "ImageCaption": {"figcaption": []},
    "Indent": {BLOCK: ["class"]},
    "Italic": {"i": []},
    "Link": {"a": ["rel", "href"]},
    "List": {"ol": [], "ul": [], "li": []},
    "ListProperties": {"ol": [], "ul": [], "li": []},
    "MediaEmbed": {
        "figure": ["class"],
        "oembed": ["url"],
        "div": ["data-oembed-url"],
        "iframe": ["frameborder", "src", "allow"],
    },
    "Mention": {"span": ["class", "data-mention"]},
    "Paragraph": {"p": []},
    "Strikethrough": {"s": []},
    "Subscript": {"sub": []},
    "Superscript": {"sup": []},
    "Table": {
        "figure": ["class"],
        "table": [],
        "thead": [],
        "tbody": [],
        "tr": [],
        "td": ["colspan", "rowspan"],
        "th": ["colspan", "rowspan"],
    },
    "TableCaption": {"figcaption": ["data-placeholder"]},
    "TableCellProperties": {"td": ["class"]},
    "TableProperties": {"figure": ["class"], "table": ["class"]},
    "TodoList": {"ul": ["class"], "label": ["class"], "span": ["class"], "li": ["class"], "input": ["class"]},
    "Underline": {"u": []},
}
BLOCKS = {"blockquote", "pre", "div", "figure", "ol", "ul", "p", "table", "tr", "td", "th"}


@lru_cache
def get_allowed_tags(config_name: str) -> Set[str]:
    """Return the list of allowed HTML tags for a given CKEditor 5 configuration."""
    return set(get_allowed_attributes(config_name))


def get_allowed_attributes(config_name: str) -> Dict[str, List[str]]:
    """Return the list of allowed HTML tags and attributes for a given CKEditor 5 configuration."""
    config = settings.CKEDITOR_5_CONFIGS.get(config_name, {})
    plugins: Iterable[str] = config.get("plugins", TAGS_BY_PLUGIN.keys())
    allowed_attributes: Dict[str, List[str]] = {}
    for plugin in plugins:
        for key, attributes in TAGS_BY_PLUGIN.get(plugin, {}).items():
            if key == BLOCK:
                keys = BLOCKS
            else:
                keys = [key]
            for key_ in keys:
                allowed_attributes.setdefault(key_, [])
                allowed_attributes[key_] += attributes
    return allowed_attributes


class CKEditor5Field(forms.CharField):
    """A form field using CKEditor 5 as text editor."""

    def __init__(self, *args, config_name="default", **kwargs) -> None:
        """Initialize the field."""
        self.ckeditor5_config = config_name
        self.required_ = kwargs.get("required", True)
        kwargs["required"] = False
        css_class = "django_ckeditor_5"
        self.is_inline_widget = "inline" in config_name
        if self.is_inline_widget:
            css_class += " ck-editor__singleline"
        kwargs["widget"] = CKEditor5Widget(attrs={"class": css_class}, config_name=config_name)
        super().__init__(*args, **kwargs)

    def to_python(self, value):
        """Convert the value to a string."""
        allowed_tags = get_allowed_tags(self.ckeditor5_config)
        allowed_attributes = get_allowed_attributes(self.ckeditor5_config)
        if value is None:
            raise ValidationError(self.error_messages["required"], code="required")
        elif len(value) <= 50 and self.required_:
            striped = html.unescape(strip_tags(value)).strip()
            if not striped:
                raise ValidationError(self.error_messages["required"], code="required")
        if self.is_inline_widget and "p" in allowed_tags:
            allowed_tags.remove("p")
        value = bleach.clean(value, strip_comments=True, strip=True, tags=allowed_tags, attributes=allowed_attributes)
        value = bleach.linkify(value)
        value = value.replace("\n", " ")
        return super().to_python(value)

    def prepare_value(self, value):
        """Prepare the value for the widget."""
        if value is None:
            return ""
        return value