"""Custom template tags for the modersite app."""

from typing import Union

from django import template
from django.conf import settings
from django.template.base import kwarg_re
from django.template.defaulttags import URLNode
from django.template.exceptions import TemplateSyntaxError
from django.utils.safestring import mark_safe

register = template.Library()

BRAND_ICONS = {
    "amazon": "amazon",
    "amazon_cognito": "amazon",
    "angellist": "angellist",
    "apple": "apple",
    "atlassian": "atlassian",
    "battlenet": "battle-net",
    "bitbucket_oauth2": "bitbucket",
    "digitalocean": "digital-ocean",
    "discord": "discord",
    "dropbox": "dropbox",
    "evernote": "evernote",
    "facebook": "facebook",
    "figma": "figma",
    "fivehundredpx": "500px",
    "flickr": "flickr",
    "foursquare": "foursquare",
    "github": "github",
    "gitlab": "gitlab",
    "google": "google",
    "hubspot": "hubspot",
    "instagram": "instagram",
    "line": "line",
    "linkedin_oauth2": "linkedin",
    "mailchimp": "mailchimp",
    "mailru": "",
    "meetup": "meetup",
    "microsoft": "microsoft",
    "odnoklassniki": "odnoklassniki",
    "openid": "openid",
    "openid_connect": "openid",
    "orcid": "orcid",
    "patreon": "patreon",
    "paypal": "paypal",
    "pinterest": "pinterest",
    "pocket": "get-pocket",
    "reddit": "reddit",
    "salesforce": "salesforce",
    "shopify": "shopify",
    "slack": "slack",
    "snapchat": "snapchat",
    "soundcloud": "soundcloud",
    "spotify": "spotify",
    "stackexchange": "stack-exchange",
    "steam": "steam",
    "strava": "strava",
    "stripe": "stripe",
    "telegram": "telegram",
    "tiktok": "tiktok",
    "trello": "trello",
    "tumblr": "tumblr",
    "twitch": "twitch",
    "twitter": "twitter",
    "twitter_oauth2": "twitter",
    "untappd": "untappd",
    "vimeo": "vimeo",
    "vimeo_oauth2": "vimeo",
    "vk": "vk",
    "weibo": "weibo",
    "weixin": "weixin",
    "windowslive": "windows",
    "xing": "xing",
    "yahoo": "yahoo",
    "yandex": "yandex",
}


@register.filter()
def abs_url(value):
    """Given a relative URL, return an absolute URL."""
    if value and value.startswith("/"):
        base_url = settings.SERVER_BASE_URL
        if base_url.endswith("/"):
            base_url = base_url[:-1]
        return mark_safe(f"{base_url}{value}")  # noqa
    return value


class AbsoluteURLNode(URLNode):
    """A template node that renders an absolute URL."""

    def render(self, context):
        """Render the URL node prefixed with the server base URL."""
        return abs_url(super().render(context))


@register.tag(name="abs_url")
def abs_url_tag(parser, token):
    """Like the default Django's url tag, but return absolute URLs."""
    bits = token.split_contents()
    if len(bits) < 2:
        raise TemplateSyntaxError(f"'{bits[0]}' takes at least one argument, a URL pattern name.")
    viewname = parser.compile_filter(bits[1])
    args = []
    kwargs = {}
    asvar = None
    bits = bits[2:]
    if len(bits) >= 2 and bits[-2] == "as":
        asvar = bits[-1]
        bits = bits[:-2]

    for bit in bits:
        match = kwarg_re.match(bit)
        if not match:
            raise TemplateSyntaxError("Malformed arguments to url tag")
        name, value = match.groups()
        if name:
            kwargs[name] = parser.compile_filter(value)
        else:
            args.append(parser.compile_filter(value))
    return AbsoluteURLNode(viewname, args, kwargs, asvar)


@register.filter
def fa6_allauth_icon(provider_id):
    """Return the font-awesome icon name for a given allauth provider."""
    return BRAND_ICONS.get(provider_id, "key")


@register.simple_tag
def fa6_icon(
    name,
    prefix="fa",
    large: Union[int, bool] = False,
    fixed: bool = False,
    spin: bool = False,
    li: bool = False,
    rotate: Union[int, bool] = None,
    border: bool = False,
    color: str = None,
):
    """Add font-awesome icons in your HTML code."""
    if isinstance(large, int) and 2 <= large <= 5:
        large = f" fa-{large:d}x"
    elif large:
        large = " fa-lg"
    else:
        large = ""
    content = '<i class="{prefix} fa-{name}{large}{fixed}{spin}{li}{rotate}{border}{color}"></i>'.format(
        prefix=prefix,
        name=name,
        large=large,
        fixed=" fa-fw" if fixed else "",
        spin=" fa-spin" if spin else "",
        li=" fa-li" if li else "",
        rotate=f" fa-rotate-{rotate}" if rotate else "",
        border=" fa-border" if border else "",
        color=f"text-{color}" if color else "",
    )
    return mark_safe(content)  # noqa
