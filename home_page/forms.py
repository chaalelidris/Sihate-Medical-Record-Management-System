from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users import models as users_models


class DoctorSignupForm(UserCreationForm):
    department = forms.ChoiceField(choices=users_models.Doctor.departments)

    class Meta:
        model = users_models.Doctor
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
        model = users_models.Patient
        fields = (
            "username",
            "first_name",
            "last_name",
            "profile_pic",
            "sexe",
            "age",
            "email",
            "address",
            "mobile",
            "symptoms",
        )


# ---------------------------------------------------------------------------
# -------------------------- for contact form -----------------------
# ---------------------------------------------------------------------------
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(
        max_length=500, widget=forms.Textarea(attrs={"rows": 3, "cols": 30})
    )
