from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from wagtail.admin.admin_url_finder import AdminURLFinder

from model_inspector.settings import exclude_app_model

admin_url_finder = AdminURLFinder()


def _get_contenttypes():
    exclude = (
        exclude_app_model
        if not hasattr(settings, "MODEL_INSPECTOR_EXCLUDE")
        or not settings.MODEL_INSPECTOR_EXCLUDE
        else settings.MODEL_INSPECTOR_EXCLUDE
    )

    exclude_apps = [app for app, _ in exclude]
    exclude_models = [model for _, model in exclude]

    return ContentType.objects.exclude(
        app_label__in=exclude_apps,
        model__in=exclude_models,
    ).order_by("app_label", "model")
