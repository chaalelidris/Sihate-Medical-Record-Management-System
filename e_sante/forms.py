from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Rdv


class PostForm(forms.ModelForm):

    class Meta:
        model = Rdv
        fields = ['date',]
    def __init__(self,*args,**kwargs):
        super(PostForm,self).__init__(*args,**kwargs)
        self.fields['date'].widget.attrs['class'] = 'datepicker'
