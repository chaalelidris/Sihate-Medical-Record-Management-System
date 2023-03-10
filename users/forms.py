from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from . import models


# ---------------------------------------------------------------------------
# -------------------------- for doctor related form ------------------------
# ---------------------------------------------------------------------------


class DoctorSignupForm(UserCreationForm):
    department = forms.ChoiceField(choices=models.Doctor.departments)

    class Meta:
        model = models.Doctor
        fields = (
            "username",
            "first_name",
            "last_name",
            "profile_pic",
            "email",
            "address",
            "mobile",
            "department",
        )
        widgets = {"password": forms.PasswordInput()}


# ---------------------------------------------------------------------------
# -------------------------- for patient related form -----------------------
# ---------------------------------------------------------------------------


class PatientSignupForm(UserCreationForm):
    symptoms = forms.CharField(max_length=100, required=True)
    mobile = forms.CharField(max_length=20, required=True)

    class Meta:
        model = models.Patient
        fields = (
            "username",
            "first_name",
            "last_name",
            "profile_pic",
            "email",
            "address",
            "mobile",
            "symptoms",
        )
        widgets = {"password": forms.PasswordInput()}


# ---------------------------------------------------------------------------
# -------------------------- for OfficeManager related form -----------------
# ---------------------------------------------------------------------------
class OfficeManagerSignupForm(UserCreationForm):
    phone_number = forms.CharField(max_length=20, required=False)

    class Meta:
        model = models.OfficeManager
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "address",
            "phone_number",
        )
        widgets = {"password": forms.PasswordInput()}


# ---------------------------------------------------------------------------
# --------------------- for consultation related form -----------------------
# ---------------------------------------------------------------------------


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = models.Consultation
        fields = "__all__"
