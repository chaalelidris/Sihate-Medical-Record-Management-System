from django import forms
from django.conf import settings
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.checks import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView

from .forms import PostForm
from .models import FichePatient, Cabinet, Rdv, Consultation, Facture, Ordonnance


def doctor(request):

    if request.user.groups.filter(name="doctor"):
        return render(request, 'pages/doctor/doctor_dashboard.html')
    else:
        # messages.info(request, '')
        return redirect('../login')


def patient(request):
    if request.user.groups.filter(name="Patients"):
        return render(request, 'pages/patient/patient_dashboard.html')
    else:
        # messages.info(request, '')
        return redirect('../login')


def logout(request):
    auth.logout(request)
    # return redirect("../login")


def rdv_new(request):
    form = PostForm(request.POST)

    if form.is_valid():
        rdv = form.save(commit=False)
        rdv.id_patient = request.user.id
        rdv.id_medecin = 1
        rdv.num_rdv = 1
        # WE NEED ID_PATIENT + ID_SEC + NUMERORDV IS STATIC PROBLEM
        rdv.save()
    context = {
        'form': form,
    }

    return render(request, 'pages/doctor/rdv_form', context)


class RdvForm(forms.ModelForm):
    class Meta:
        model = Rdv
        fields = ['date', 'num_rdv']


def CountNumeroRdv():
    no = Rdv.objects.count()
    if no == None:
        return 1
    else:
        return no + 1


@login_required
def rdv_list(request):
    rdv = Rdv.objects.all()
    return render(request, 'pages/doctor/rdv_list.html', {'rdv': rdv})


@login_required
def rdv_create(request, template_name='pages/doctor/rdv_form.html'):
    form = RdvForm(request.POST or None)

    if form.is_valid():
        rdv = form.save(commit=False)
        rdv.id_patient = request.user
        rdv.num_rdv = CountNumeroRdv()
        rdv.save()
        return redirect('rdv_list')
    return render(request, template_name, {'form': form})


@login_required
def rdv_update(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    rdv = get_object_or_404(Rdv, id=id)

    form = RdvForm(request.POST or None, instance=rdv)

    if form.is_valid():

        form.save()
        return redirect("rdv_list")

    context["form"] = form

    return render(request, "pages/doctor/rdv_form.html", context)


@login_required
def rdv_delete(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    rdv = get_object_or_404(Rdv, id=id)

    if request.method == "POST":

        rdv.delete()
        rdv.num_rdv = CountNumeroRdv()

        return redirect("rdv_list")

    return render(request, "pages/doctor/rdv_confirm_delete.html", context)


class PatientForm(forms.ModelForm):
    class Meta:
        model = FichePatient
        fields = ['nom', 'prenom', 'age', 'sexe']


def patient_list(request, template_name='pages/doctor/patient_list.html'):
    patient = FichePatient.objects.all()
    return render(request, template_name, {'patient': patient})


class OrdonnanceForm(forms.ModelForm):
    class Meta:
        model = Ordonnance
        fields = ['date', 'medicament', 'observation']


def ordonnance_list(request, template_name='pages/doctor/ordonnance_list.html'):
    ordonnance = Ordonnance.objects.all()
    return render(request, template_name, {'ordonnance': ordonnance})


def ordonnance(request, template_name='pages/doctor/ordonnance.html'):
    form = OrdonnanceForm(request.POST or None)

    if form.is_valid():
        ordonnance = form.save(commit=False)
        ordonnance.save()
        return redirect('ordonnance_list')
    return render(request, template_name, {'form': form})


def ordonnance_edit(request, id_ordonnance):
    # dictionary for initial data with
    # field names as keys
    context = {}

    ordonnance = get_object_or_404(Ordonnance, id_ordonnance=id_ordonnance)

    form = OrdonnanceForm(request.POST or None, instance=ordonnance)

    if form.is_valid():

        form.save()
        return redirect("ordonnance_list")

    context["form"] = form

    return render(request, "pages/doctor/ordonnance.html", context)


@login_required
def ordonnance_delete(request, id_ordonnance):
    # dictionary for initial data with
    # field names as keys
    context = {}

    ordonnance = get_object_or_404(Ordonnance, id_ordonnance=id_ordonnance)

    if request.method == "POST":

        ordonnance.delete()

        return redirect("ordonnance_list")

    return render(request, "pages/doctor/ordonnance_delete.html", context)
