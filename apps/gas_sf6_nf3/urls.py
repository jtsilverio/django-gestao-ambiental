from django.urls import path

from apps.gas_sf6_nf3 import views

app_name = "gas_sf6_nf3"

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "cadastro/",
        views.Create.as_view(),
        name="create",
    ),
    path(
        "edit/<int:pk>/",
        views.Edit.as_view(),
        name="edit",
    ),
    path(
        "delete/<int:pk>/",
        views.delete,
        name="delete",
    ),
]
