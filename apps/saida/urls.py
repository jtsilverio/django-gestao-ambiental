from django.urls import path

from apps.saida import views

app_name = "saida"

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
]
