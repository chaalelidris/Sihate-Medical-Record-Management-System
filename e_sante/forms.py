from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Rdv, Consultation, Profile, FichePatient


class PostForm(forms.ModelForm):

    class Meta:
        model = Rdv
        fields = ['date', ]

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['class'] = 'datepicker'


class DataFrom(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = '__all__'


class EditProfileForm(UserChangeForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'w3-input w3-border w3-round', 'placeholder': 'password'}))

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password',
        )
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'w3-input w3-border w3-round', 'placeholder': 'first name'}),
            'last_name': forms.TextInput(attrs={'class': 'w3-input w3-border w3-round', 'placeholder': 'last name'}),
            'email': forms.EmailInput(attrs={'class': 'w3-input w3-border w3-round', 'placeholder': 'email'}),
            'username': forms.TextInput(attrs={'class': 'w3-input w3-border w3-round', 'placeholder': 'username'}),

        }


class fiche_patientForm(forms.ModelForm):
    class Meta:
        model = FichePatient
        fields = '__all__'
        widgets = {
            'id_patient': forms.Select(attrs={'class': 'w3-input w3-border w3-round', }),
            'id_medecin': forms.Select(attrs={'class': 'w3-input w3-border w3-round', }),
            'nom': forms.TextInput(attrs={'class': 'w3-input w3-border w3-round', }),
            'prenom': forms.TextInput(attrs={'class': 'w3-input w3-border w3-round', }),
            'address': forms.TextInput(attrs={'class': 'w3-input w3-border w3-round', }),
            'age': forms.NumberInput(attrs={'class': 'w3-input w3-border w3-round', }),
            'sexe': forms.Select(attrs={'class': 'w3-input w3-border w3-round', }),
            'tel': forms.NumberInput(attrs={'class': 'w3-input w3-border w3-round', }),
            'email': forms.EmailInput(attrs={'class': 'w3-input w3-border w3-round', }),
            'group_sanguin': forms.Select(attrs={'class': 'w3-input w3-border w3-round', }),
            'NSS': forms.TextInput(attrs={'class': 'w3-input w3-border w3-round', }),
            'profession': forms.TextInput(attrs={'class': 'w3-input w3-border w3-round', }),
            'motif_consultation': forms.TextInput(attrs={'class': 'w3-input w3-border w3-round', }),
            'nom_etablissement_universitaire': forms.TextInput(attrs={'class': 'w3-input w3-border w3-round', }),
            'date_naiss': forms.DateTimeInput(attrs={'class': 'w3-input w3-border w3-round', }),
            'lieu_naiss': forms.TextInput(attrs={'class': 'w3-input w3-border w3-round', }),
            'situation': forms.Select(attrs={'class': 'w3-input w3-border w3-round', }),
            'filiére': forms.TextInput(attrs={'class': 'w3-input w3-border w3-round', }),
            'à_fumer': forms.Select(attrs={'class': 'w3-input w3-border w3-round', }),
            'à_chiquer': forms.Select(attrs={'class': 'w3-input w3-border w3-round', }),
            'à_prise': forms.Select(attrs={'class': 'w3-input w3-border w3-round', }),
            'nbr_cigarettes': forms.NumberInput(attrs={'class': 'w3-input w3-border w3-round', }),
            'nbr_boites': forms.NumberInput(attrs={'class': 'w3-input w3-border w3-round', }),
            'age_à_la_premiére_prise': forms.NumberInput(attrs={'class': 'w3-input w3-border w3-round', }),
            'ancien_fumeur': forms.Select(attrs={'class': 'w3-input w3-border w3-round', }),
            'periode_exposition': forms.NumberInput(attrs={'class': 'w3-input w3-border w3-round', }),
            'Affections_congénitales': forms.Textarea(attrs={'class': 'w3-input w3-border w3-round', }),
            'Maladies_génerale': forms.Textarea(attrs={'class': 'w3-input w3-border w3-round', }),
            'Interventions_chirurgicales': forms.Textarea(attrs={'class': 'w3-input w3-border w3-round', }),
            'Réactions_allergique_aux_médicaments': forms.Textarea(attrs={'class': 'w3-input w3-border w3-round', }),
        }
