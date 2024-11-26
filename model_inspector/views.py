import django_filters
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.forms import CheckboxSelectMultiple
from django.utils.translation import gettext_lazy as _
from wagtail.admin.admin_url_finder import AdminURLFinder
from wagtail.admin.filters import WagtailFilterSet
from wagtail.admin.views.reports import ReportView
from wagtail.models import Page

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


class AdminURLFinder(AdminURLFinder):
    def get_edit_url(self, instance):
        try:
            return super().get_edit_url(instance)
        except AttributeError:
            return None


admin_url_finder = AdminURLFinder()


def _get_contenttypes():
    exclude = (
        exclude_app_model
        if not hasattr(settings, "MODEL_INSPECTOR_CONTENT_TYPES_EXCLUDE")
        else settings.MODEL_INSPECTOR_CONTENT_TYPES_EXCLUDE
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

        for ct in ctx["object_list"]:
            # wagtail pages
            if issubclass(ct.model_class(), Page):
                first_instance = ct.model_class().objects.live().first()
                # get the frontend url for the content type
                ct.frontend_url = None
                try:
                    ct.frontend_url = first_instance.get_url()
                except AttributeError:
                    pass
            else:
                first_instance = ct.model_class().objects.first()

            # get the admin edit url for the content type
            ct.admin_edit_url = None
            try:
                ct.admin_edit_url = admin_url_finder.get_edit_url(first_instance)
            except AttributeError:
                pass

        return ctx

    def get_queryset(self):
        qs = _get_contenttypes()

        search_query = self.request.GET.get("q")
        if search_query:
            qs = qs.filter(
                Q(app_label__icontains=search_query) | Q(model__icontains=search_query)
            )

        return qs
