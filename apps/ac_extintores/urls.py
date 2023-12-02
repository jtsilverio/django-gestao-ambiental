from django.urls import path

from apps.ac_extintores import views

app_name = "ac_extintores"

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
