from django import forms
from appointment.models import Appointment
from .models import MedicalRecord


# ---------------------------------------------------------------------------------------------
# ------------------------------------- MedicaRecordForm --------------------------------------
# ---------------------------------------------------------------------------------------------
class medicaRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = "__all__"


# ---------------------------------------------------------------------------------------------
# ------------------------------------- PrescriptionForm --------------------------------------
# ---------------------------------------------------------------------------------------------
class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ["patient", "date_prescribed", "medication", "observation"]
