from django.db import models
from wagtail.admin.panels import FieldPanel, TitleFieldPanel
from wagtail.models import Page


class BlogPage(Page):
    pass


class BlogIndexPage(Page):
    pass


class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name_plural = "blog categories"
        verbose_name = "blog category"

    def __str__(self):
        return f"{self.name} - {self.slug}"

    panels = [
        TitleFieldPanel("name"),
        FieldPanel("slug"),
    ]
