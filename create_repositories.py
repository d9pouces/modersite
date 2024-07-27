"""Create repositories."""

# Description: Create a new repository in Read the Docs
{
    "name": "Test Project",
    "repository": {"url": "https://github.com/readthedocs/template", "type": "git"},
    "homepage": "http://template.readthedocs.io/",
    "programming_language": "py",
    "language": "es",
    "privacy_level": "public",
    "external_builds_privacy_level": "public",
    "tags": ["automation", "sphinx"],
}
# curl \
#   -X POST \
#   -H "Authorization: Token <token>" https://readthedocs.org/api/v3/projects/ \
#   -H "Content-Type: application/json" \
#   -d @body.json
