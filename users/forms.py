from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from . import models


# ---------------------------------------------------------------------------
# -------------------------- for doctor related form ------------------------
# ---------------------------------------------------------------------------


class DoctorSignupForm(UserCreationForm):
    department = forms.ChoiceField(choices=models.Doctor.departments)

    class Meta(UserCreationForm.Meta):
        model = models.Doctor
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "address",
            "mobile",
            "department",
            "password1",
            "password2",
        )


# ---------------------------------------------------------------------------
# -------------------------- for patient related form -----------------------
# ---------------------------------------------------------------------------


class PatientSignupForm(UserCreationForm):
    symptoms = forms.CharField(max_length=100, required=True)
    mobile = forms.CharField(max_length=20, required=True)

    class Meta(UserCreationForm.Meta):
        model = models.Patient
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "address",
            "mobile",
            "symptoms",
            "password1",
            "password2",
        )


# ---------------------------------------------------------------------------
# -------------------------- for OfficeManager related form -----------------
# ---------------------------------------------------------------------------
class OfficeManagerSignupForm(UserCreationForm):
    phone_number = forms.CharField(max_length=20, required=False)

    class Meta(UserCreationForm.Meta):
        model = models.OfficeManager
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "address",
            "phone_number",
            "password1",
            "password2",
        )


# ---------------------------------------------------------------------------
# --------------------- for consultation related form -----------------------
# ---------------------------------------------------------------------------


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = models.Consultation
        fields = "__all__"
