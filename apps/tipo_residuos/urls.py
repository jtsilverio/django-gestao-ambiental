from django.urls import path

from apps.tipo_residuos import views

app_name = "tipo_residuos"

urlpatterns = [
    path("", views.index, name="index"),
    path("cadastro/", views.Create.as_view(), name="create"),
    path("edit/<int:pk>/", views.Edit.as_view(), name="edit"),
    path("delete/<int:pk>/", views.delete, name="delete"),
    path("get_class/", views.get_class, name="get_class"),
]
