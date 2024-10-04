# Generated by Django 5.1.1 on 2024-10-04 16:45

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("style_guide", "0005_alter_picoblockspage_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="picoblockspage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    ("paragraph", 0),
                    ("table", 1),
                    ("accordion", 6),
                    ("image", 7),
                    ("embed", 8),
                ],
                blank=True,
                block_lookup={
                    0: ("wagtail.blocks.RichTextBlock", (), {"required": False}),
                    1: (
                        "wagtail.contrib.table_block.blocks.TableBlock",
                        (),
                        {"required": False, "table_options": {"minSpareRows": 0}},
                    ),
                    2: ("wagtail.blocks.CharBlock", (), {}),
                    3: ("wagtail.blocks.RichTextBlock", (), {}),
                    4: ("wagtail.blocks.BooleanBlock", (), {"default": False}),
                    5: (
                        "wagtail.blocks.StructBlock",
                        [[("title", 2), ("content", 3), ("initially_open", 4)]],
                        {"max_num": 4, "min_num": 1},
                    ),
                    6: ("wagtail.blocks.ListBlock", (5,), {}),
                    7: ("wagtail.images.blocks.ImageChooserBlock", (), {}),
                    8: ("wagtail.embeds.blocks.EmbedBlock", (), {}),
                },
            ),
        ),
    ]