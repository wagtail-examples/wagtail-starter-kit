from django.urls import path

from model_inspector import views

app_name = "model_inspector"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("results/", views.IndexView.as_view(results_only=True), name="index_results"),
]
