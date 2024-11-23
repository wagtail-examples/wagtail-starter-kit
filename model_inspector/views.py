from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _

from wagtail.admin.views.reports import ReportView


exclude_app_model = [
    ("wagtailcore", "page"),
    # ("home", "homepage"),
    ("wagtailadmin", "admin"),
    ("wagtailcore", "groupapprovaltask"),
    ("wagtailcore", "locale"),
    # ("wagtailcore", "site"),
    ("wagtailcore", "modellogentry"),
    ("wagtailcore", "collectionviewrestriction"),
    # ("wagtailcore", "collection"),
    ("wagtailcore", "groupcollectionpermission"),
    ("wagtailcore", "uploadedfile"),
    ("wagtailcore", "referenceindex"),
    ("wagtailcore", "revision"),
    ("wagtailcore", "grouppagepermission"),
    ("wagtailcore", "pageviewrestriction"),
    ("wagtailcore", "workflowpage"),
    ("wagtailcore", "workflowcontenttype"),
    # ("wagtailcore", "workflowtask"),
    ("wagtailcore", "task"),
    # ("wagtailcore", "workflow"),
    ("wagtailcore", "workflowstate"),
    ("wagtailcore", "taskstate"),
    ("wagtailcore", "pagelogentry"),
    ("wagtailcore", "comment"),
    ("wagtailcore", "commentreply"),
    ("wagtailcore", "pagesubscription"),
    # ("wagtaildocs", "document"),
    # ("wagtailimages", "image"),
    # ("wagtailforms", "formsubmission"),
    # ("wagtailredirects", "redirect"),
    ("wagtailembeds", "embed"),
    # ("wagtailusers", "userprofile"),
    ("wagtailimages", "rendition"),
    ("wagtailsearch", "indexentry"),
    ("wagtailadmin", "editingsession"),
    ("taggit", "tag"),
    ("taggit", "taggeditem"),
    ("admin", "logentry"),
    ("auth", "permission"),
    ("auth", "group"),
    ("auth", "user"),
    ("contenttypes", "contenttype"),
    ("sessions", "session"),
]


class ContenttypesReportView(ReportView):
    results_template_name = "reports/contenttypes_report_results.html"
    page_title = _("Contenttypes Report")
    header_icon = "key"
    index_url_name = "contenttypes_report"
    index_results_url_name = "contenttypes_report_results"

    context_object_name = "contenttypes"

    search_fields = [
        "app_label",
        "model",
    ]

    def get_queryset(self):
        exclude = (
            exclude_app_model
            if not hasattr(settings, "MODEL_INSPECTOR_CONTENT_TYPES_EXCLUDE")
            else settings.MODEL_INSPECTOR_CONTENT_TYPES_EXCLUDE
        )

        exclude_apps = [app for app, _ in exclude]
        exclude_models = [model for _, model in exclude]

        qs = ContentType.objects.exclude(
            app_label__in=exclude_apps,
            model__in=exclude_models,
        ).order_by("app_label", "model")
        
        return qs
