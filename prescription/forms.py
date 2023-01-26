from django import forms
from .models import Prescription


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ["name_patient", "date", "medicament", "observation"]
