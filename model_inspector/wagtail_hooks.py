from django.templatetags.static import static
from django.urls import include, path, reverse
from django.utils.html import format_html
from wagtail import hooks
from wagtail.admin.menu import AdminOnlyMenuItem

from model_inspector import urls


@hooks.register("insert_global_admin_js")
def copy_script():
    return format_html(
        '<script src="{0}"></script>',
        static("model_inspector/js/copy.js"),
    )


@hooks.register("register_admin_urls")
def register_admin_urls():
    return [
        path("model-inspector/", include(urls, namespace="model_inspector")),
    ]


@hooks.register("register_settings_menu_item")
def register_model_inspector_menu_item():
    return AdminOnlyMenuItem(
        "Model Inspector",
        reverse("model_inspector:index"),
        icon_name="cog",
        order=10000,
    )
