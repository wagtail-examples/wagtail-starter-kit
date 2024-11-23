from .base import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-i7bqh5eiw93f*$d6q_#$506gp%w8@xvo0nu77f_j&g&yt-zh38"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Remove if not required
INSTALLED_APPS += ["app.style_guide", "wagtail.contrib.styleguide"]  # noqa F405

# MODEL_INSPECTOR_CONTENT_TYPES_EXCLUDE = [
#     # ("wagtailadmin", "admin"),
#     # ("contenttypes", "contenttype"),
# ]

try:
    from .local import *  # noqa
except ImportError:
    pass
