from django.apps import AppConfig


class ModelInspectorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'model_inspector'
