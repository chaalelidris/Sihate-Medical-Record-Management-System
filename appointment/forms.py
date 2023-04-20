from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    date = forms.DateTimeField(
        input_formats=["%Y-%m-%d %H:%M:%S"],
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
    )

    class Meta:
        model = Appointment
        fields = ["doctor", "patient", "date", "description"]
        labels = {
            "doctor": "Doctor",
            "patient": "Patient",
            "date": "Date and Time",
            "description": "Description",
        }


class AppointmentUpdateForm(forms.ModelForm):
    date = forms.DateTimeField(
        input_formats=["%Y-%m-%d %H:%M:%S"],
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
    )

    class Meta:
        model = Appointment
        fields = ["doctor", "patient", "date", "description"]
        labels = {
            "doctor": "Doctor",
            "patient": "Patient",
            "date": "Date and Time",
            "description": "Description",
        }
