from django import template

from app.blog.models import BlogIndexPage

register = template.Library()


@register.simple_tag
def get_blog_index_url():
    blog_index = BlogIndexPage.objects.live().first()
    if blog_index:
        return blog_index.url
