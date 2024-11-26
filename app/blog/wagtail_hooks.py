from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from app.blog.models import BlogCategory


class BlogCategorySnippetViewset(SnippetViewSet):
    model = BlogCategory


register_snippet(BlogCategory)
