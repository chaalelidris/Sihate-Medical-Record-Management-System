from django import forms
from .models import Consultation


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = [
            "id_consultation",
            "id_patient",
            "contenue",
            "antecedant",
            "traitement",
            "date_consultation",
        ]
