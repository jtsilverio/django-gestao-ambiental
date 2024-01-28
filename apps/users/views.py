from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from apps.users.forms import LoginForm, RegisterForm
from decorators.login_exempt import login_exempt

APP_NAME = "users"
APP_TITLE = "Usuários"


@login_exempt
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                next_url = request.POST.get("next", "/")
                return redirect(next_url)
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()

    context = {"form": form, "next": request.GET.get("next", "/")}
    return render(request, "users/login.html", context)


@login_exempt
def user_logout(request):
    logout(request)
    return redirect("users:login")


def create_user(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuário cadastrado.")  # Add success message
            return redirect("users:create")

    context = {
        "form": form,
        "title": APP_TITLE,
        "app_name": APP_NAME,
    }

    return render(request, "users/create.html", context)
