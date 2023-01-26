from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms


class EditProfileForm(UserChangeForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "w3-input w3-border w3-round", "placeholder": "password"}
        )
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
            "password",
        )
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "w3-input w3-border w3-round",
                    "placeholder": "first name",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "w3-input w3-border w3-round",
                    "placeholder": "last name",
                }
            ),
            "email": forms.EmailInput(
                attrs={"class": "w3-input w3-border w3-round", "placeholder": "email"}
            ),
            "username": forms.TextInput(
                attrs={
                    "class": "w3-input w3-border w3-round",
                    "placeholder": "username",
                }
            ),
        }
