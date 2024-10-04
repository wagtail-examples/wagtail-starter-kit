from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page


class PicoBlocksPage(Page):
    body = StreamField(
        [
            ("paragraph", blocks.RichTextBlock(required=False)),
            ("table", TableBlock(table_options={"minSpareRows": 0}, required=False)),
            (
                "accordion",
                blocks.ListBlock(
                    blocks.StructBlock(
                        [
                            ("title", blocks.CharBlock()),
                            ("content", blocks.RichTextBlock()),
                            (
                                "initially_open",
                                blocks.BooleanBlock(default=False, required=False),
                            ),
                        ],
                        min_num=1,
                        max_num=4,
                    ),
                ),
            ),
            ("image", ImageChooserBlock()),
            ("embed", EmbedBlock()),
        ],
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]
