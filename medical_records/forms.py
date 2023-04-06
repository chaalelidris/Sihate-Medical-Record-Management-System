from django import forms
from appointment.models import Appointment
from .models import MedicalRecord


class medicaRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = "__all__"
