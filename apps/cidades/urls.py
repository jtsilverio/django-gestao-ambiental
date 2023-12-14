from django.urls import path

from apps.cidades import views

app_name = "cidades"

urlpatterns = [
    path("get_cidades/", views.get_cidades, name="get_cidades"),
]
