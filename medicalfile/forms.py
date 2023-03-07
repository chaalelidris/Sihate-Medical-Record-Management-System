from django import forms
from appointment.models import Appointment
from medicalfile.models import MedicalFile


class medicalFileForm(forms.ModelForm):
    class Meta:
        model = MedicalFile
        fields = "__all__"
