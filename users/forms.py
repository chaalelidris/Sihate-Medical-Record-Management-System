from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from phonenumber_field.formfields import PhoneNumberField
from . import models as users_models


# ---------------------------------------------------------------------------
# -------------------------- for doctor related form -----------------------
# ---------------------------------------------------------------------------
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


class DoctorUpdateForm(UserChangeForm):
    class Meta:
        model = users_models.Doctor
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "mobile",
            "profile_pic",
            "department",
            "address",
        )

        widgets = {
            "profile_pic": forms.ClearableFileInput(attrs={"multiple": False}),
        }

    def clean_mobile(self):
        mobile = self.cleaned_data["mobile"]
        if len(mobile) != 10:
            raise forms.ValidationError("Mobile number must be 10 digits long.")
        return mobile


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
            "gender",
            "age",
            "email",
            "address",
            "mobile",
            "symptoms",
        )

    def clean_mobile(self):
        mobile = self.cleaned_data["mobile"]
        if len(mobile) != 10:
            raise forms.ValidationError("Mobile number must be 10 digits long.")
        return mobile


class PatientUpdateForm(UserChangeForm):
    symptoms = forms.CharField(max_length=100, required=True)
    mobile = forms.CharField(max_length=20, required=True)

    class Meta:
        model = users_models.Patient
        fields = (
            "username",
            "first_name",
            "last_name",
            "profile_pic",
            "gender",
            "age",
            "email",
            "address",
            "mobile",
            "symptoms",
        )

    def clean_mobile(self):
        mobile = self.cleaned_data["mobile"]
        if len(mobile) != 10:
            raise forms.ValidationError("Mobile number must be 10 digits long.")
        return mobile


# ---------------------------------------------------------------------------
# -------------------------- for manager related form -----------------------
# ---------------------------------------------------------------------------
class ManagerUpdateForm(forms.ModelForm):
    class Meta:
        model = users_models.OfficeManager
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "address",
            "mobile",
            "profile_pic",
        ]

    mobile = PhoneNumberField(required=False)
