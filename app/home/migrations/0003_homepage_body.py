# Generated by Django 5.1.1 on 2024-10-06 12:19

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_create_homepage"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="body",
            field=wagtail.fields.RichTextField(blank=True),
        ),
    ]
