from django.urls import path

from apps.users import views

app_name = "users"

urlpatterns = [
    path("login/", views.login_user, name="login"),
]
