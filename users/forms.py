from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from . import models


# ---------------------------------------------------------------------------
# -------------------------- for doctor related form ------------------------
# ---------------------------------------------------------------------------
class UserCreationForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = ["username", "first_name", "last_name", "password"]


class UserChangeForm(UserChangeForm):
    class Meta:
        model = models.User
        fields = ["username", "first_name", "last_name", "password"]


class DoctorForm(forms.ModelForm):
    class Meta:
        model = models.Doctor
        fields = ["address", "mobile", "department", "status", "profile_pic"]


# ---------------------------------------------------------------------------
# --------------------- for consultation related form -----------------------
# ---------------------------------------------------------------------------


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = models.Consultation
        fields = "__all__"
