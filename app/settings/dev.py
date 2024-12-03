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

MODEL_INSPECTOR_EXCLUDE = [
    ("admin", "logentry"),
    ("auth", "group"),
    ("auth", "permission"),
    ("contenttypes", "contenttype"),
    ("forms", "formfield"),
    ("sessions", "session"),
    ("taggit", "tag"),
    ("taggit", "taggeditem"),
    ("wagtailadmin", "admin"),
    ("wagtailcore", "collectionviewrestriction"),
    ("wagtailadmin", "editingsession"),
    ("wagtailcore", "comment"),
    ("wagtailcore", "commentreply"),
    ("wagtailcore", "groupapprovaltask"),
    ("wagtailcore", "groupcollectionpermission"),
    ("wagtailcore", "grouppagepermission"),
    ("wagtailcore", "locale"),
    ("wagtailcore", "modellogentry"),
    ("wagtailcore", "pagelogentry"),
    ("wagtailcore", "pagesubscription"),
    ("wagtailcore", "pageviewrestriction"),
    ("wagtailcore", "referenceindex"),
    ("wagtailcore", "revision"),
    ("wagtailcore", "taskstate"),
    ("wagtailcore", "uploadedfile"),
    ("wagtailcore", "workflowcontenttype"),
    ("wagtailcore", "workflowpage"),
    ("wagtailcore", "workflowstate"),
    ("wagtailcore", "workflowtask"),
    ("wagtailembeds", "embed"),
    ("wagtailforms", "formsubmission"),
    ("wagtailimages", "rendition"),
    ("wagtailsearch", "indexentry"),
    ("wagtailusers", "userprofile"),
    ("wagtailcore", "page"),
]

try:
    from .local import *  # noqa
except ImportError:
    pass
