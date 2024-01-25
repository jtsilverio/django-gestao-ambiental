# create a login form
# Path: apps/users/forms.py
from django import forms


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
