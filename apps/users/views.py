from django.shortcuts import render

from apps.users.forms import LoginForm


# Create your views here.
def login_user(request):
    form = LoginForm()
    context = {"form": form}
    return render(request, "users/login.html", context)
