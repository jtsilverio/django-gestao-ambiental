from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from apps.users.forms import LoginForm
from decorators.login_exempt import login_exempt


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
