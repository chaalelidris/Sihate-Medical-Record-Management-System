from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import FichePatient,Cabinet,Rdv,Consultation,Ordonnance,Profile

admin.site.register(Cabinet)
admin.site.register(FichePatient)
admin.site.register(Rdv)
admin.site.register(Consultation)
admin.site.register(Ordonnance)
admin.site.register(Profile)