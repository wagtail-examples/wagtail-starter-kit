import django_filters
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.forms import CheckboxSelectMultiple
from django.utils.translation import gettext_lazy as _
from wagtail.admin.admin_url_finder import AdminURLFinder
from wagtail.admin.filters import WagtailFilterSet
from wagtail.admin.views.reports import ReportView

exclude_app_model = [
    ("admin", "logentry"),
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


class ContentTypeFilterSet(WagtailFilterSet):
    app_label = django_filters.MultipleChoiceFilter(
        field_name="app_label",
        lookup_expr="iexact",
        widget=CheckboxSelectMultiple,
        label=_("App label"),
    )
    model = django_filters.MultipleChoiceFilter(
        field_name="model",
        lookup_expr="iexact",
        widget=CheckboxSelectMultiple,
        label=_("Model"),
    )

    class Meta:
        model = ContentType
        fields = []

    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super().__init__(data=data, queryset=queryset, request=request, prefix=prefix)

        self.queryset = _get_contenttypes()

        self.filters["app_label"].extra["choices"] = sorted(
            {(ct.app_label, ct.app_label) for ct in self.queryset}
        )

        self.filters["model"].extra["choices"] = sorted(
            [(ct.model, ct.model) for ct in self.queryset]
        )


class ContenttypesReportView(ReportView):
    results_template_name = "reports/contenttypes_report_results.html"
    page_title = _("Content Types")
    header_icon = "key"
    index_url_name = "contenttypes_report"
    index_results_url_name = "contenttypes_report_results"

    context_object_name = "contenttypes"
    filterset_class = ContentTypeFilterSet
    is_searchable = True

    search_fields = [
        "app_label",
        "model",
    ]

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)

        for contenttype in ctx["object_list"]:
            self.generate_urls_for_report_view(
                contenttype, contenttype.model_class().objects.first()
            )

        return ctx

    def generate_urls_for_report_view(self, contenttype, first_instance):
        try:
            contenttype.frontend_url = first_instance.get_url()
        except AttributeError:
            contenttype.frontend_url = None

        contenttype.admin_edit_url = admin_url_finder.get_edit_url(first_instance)

    def get_queryset(self):
        qs = _get_contenttypes()
        # qs = ContentType.objects.all().order_by("app_label", "model")

        search_query = self.request.GET.get("q")
        if search_query:
            qs = qs.filter(
                Q(app_label__icontains=search_query) | Q(model__icontains=search_query)
            )

        return qs
