from django.urls import path

from apps.fornecedor import views

app_name = "fornecedor"

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "cadastro/",
        views.Create.as_view(),
        name="cadastro",
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
    path(
        "get_destinacao/",
        views.get_destinacao,
        name="get_destinacao",
    ),
]
