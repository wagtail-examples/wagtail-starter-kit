from django.urls import path, reverse
from django.utils.safestring import mark_safe

from wagtail.admin.menu import AdminOnlyMenuItem
from wagtail import hooks

from .views import ContenttypesReportView


@hooks.register("register_reports_menu_item")
def register_unpublished_changes_report_menu_item():
    return AdminOnlyMenuItem(
        "Contentypes",
        reverse("contenttypes_report"),
        icon_name=ContenttypesReportView.header_icon,
        order=700,
    )


@hooks.register("register_admin_urls")
def register_unpublished_changes_report_url():
    return [
        path(
            "reports/contenttypes/",
            ContenttypesReportView.as_view(),
            name="contenttypes_report",
        ),
        # Add a results-only view to add support for AJAX-based filtering
        path(
            "reports/contenttypes/results/",
            ContenttypesReportView.as_view(results_only=True),
            name="contenttypes_report_results",
        ),
    ]


@hooks.register("insert_global_admin_js")
def editor_js():
    return mark_safe(
        """
        <script>
        document.addEventListener('DOMContentLoaded', function() {
            const buttons = document.querySelectorAll('button[data-model-inspector-copy]');
            buttons.forEach((button) => {
                button.addEventListener('click', function() {
                    const code = this.closest('tr').querySelector('code').innerText;
                    const buttonInnerText = this.querySelector('span:last-child');
                    const buttonOriginalInnerText = buttonInnerText.innerText;

                    navigator.clipboard.writeText(code).then(function () {
                        buttonInnerText.innerText = 'Copied!';
                        button.setAttribute('disabled', true);
                        setTimeout(() => {
                            buttonInnerText.innerText = buttonOriginalInnerText;
                            button.removeAttribute('disabled');
                        }, 1000);
                    });
                });
            });
        });
        </script>
        """,
    )
