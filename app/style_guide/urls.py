from django.urls import path

from app.style_guide import views

urlpatterns = [
    path("", views.style_guide_view, name="style-guide"),
]
