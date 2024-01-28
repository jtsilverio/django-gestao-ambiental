# create a login form
# Path: apps/users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        label="Username",
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Username", "class": "form-control"}
        ),
    )

    password = forms.CharField(
        max_length=50,
        required=True,
        label="Password",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-control"}
        ),
    )


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        help_text="Required. Inform a valid email address.",
        widget=forms.EmailInput(attrs={"class": "form-control"}),
    )
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "Email already exists, please use another email."
            )

        return email

    def clean_username(self):
        username = self.cleaned_data["username"]

        if len(username) > 20:
            raise forms.ValidationError(
                "Nome de usuário deve ter no máximo 20 caracteres."
            )

        if " " in username:
            raise forms.ValidationError("Nome de usuário não pode conter espaços.")

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                "Username already exists, please use another username."
            )

        return username
