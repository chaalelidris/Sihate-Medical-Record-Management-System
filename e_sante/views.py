from itertools import count

from django import forms
from django.conf import settings
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.checks import messages
from django.db.models import Count
from django.http import HttpResponseRedirect, response
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from django.views.generic import TemplateView
#from notifications.signals import notify

from .forms import PostForm, EditProfileForm, fiche_patientForm
from .models import FichePatient, Cabinet, Rdv, Consultation, Ordonnance, Profile
from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from .forms import DataFrom


def doctor(request):

    if request.user.groups.filter(name="doctor"):
        return render(request, 'pages/doctor/doctor_dashboard.html')
    else:
        # messages.info(request, '')
        return redirect('../login')


def doctor_profile(request):

    user = request.user
    form = EditProfileForm(request.POST or None, instance=request.user)

    if request.method == 'POST':

        if form.is_valid():

            form.save()
            new_password = form.cleaned_data.get('password')
            if new_password:
                user.set_password(new_password)
                form.save(new_password)

            return HttpResponseRedirect(reverse('doctor'))

    context = {"form": form, }

    return render(request, 'pages/doctor/doctor_profile.html', context)


def patient_profile(request):
    user = request.user
    form = EditProfileForm(request.POST or None, instance=user)
    if request.method == 'POST':
        if form.is_valid():

            form.save()

            new_password = form.cleaned_data.get('password')
            if new_password:
                user.set_password(new_password)
                form.save(new_password)

            return HttpResponseRedirect(reverse('patient'))

    context = {"form": form}

    return render(request, 'pages/patient/patient_profile.html', context)


def patient(request):
    if request.user.groups.filter(name="Patients"):
        return render(request, 'pages/patient/patient_dashboard.html')
    else:
        # messages.info(request, '')
        return redirect('../login')


def ESI(request):
    if request.user.groups.filter(name="ESI"):
        return render(request, 'pages/ESI/ESI_dashboard.html')
    else:
        # messages.info(request, '')
        return redirect('../login')


def ESI_profile(request):
    user = request.user
    form = EditProfileForm(request.POST or None, instance=user)
    if request.method == 'POST':
        if form.is_valid():

            form.save()

            new_password = form.cleaned_data.get('password')
            if new_password:
                user.set_password(new_password)
                form.save(new_password)

            return HttpResponseRedirect(reverse('ESI'))

    context = {"form": form}

    return render(request, 'pages/ESI/ESI_profile.html', context)


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
        fields = ['id_patient', 'date', 'num_rdv']
        widgets = {
            'id_patient': forms.Select(attrs={'class': 'w3-input w3-border w3-round', }),
            'date': forms.TextInput(attrs={'class': 'w3-input w3-border w3-round', }),
            'num_rdv': forms.NumberInput(attrs={'class': 'w3-input w3-border w3-round', }),
        }


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
        fields = ['nom', 'prenom', 'age', 'sexe', 'email']


def patient_list(request, template_name='pages/doctor/patient_list.html'):
    fiche_patient = FichePatient.objects.all()
    return render(request, template_name, {'fiche_patient': fiche_patient})


@login_required()
def fiche_patient(request, template_name='pages/doctor/fiche_patient.html'):
    form = fiche_patientForm(request.POST or None)

    if form.is_valid():
        fiche_patient = form.save(commit=False)
        fiche_patient.save()
        return redirect('patient_list')
    return render(request, template_name, {'form': form})


@login_required()
def fiche_patient_edit(request, id_fiche):
    # dictionary for initial data with
    # field names as keys
    context = {}

    fiche_patient = get_object_or_404(FichePatient, id_fiche=id_fiche)

    form = fiche_patientForm(request.POST or None, instance=fiche_patient)

    if form.is_valid():

        form.save()
        return redirect("patient_list")

    context["form"] = form

    return render(request, "pages/doctor/fiche_patient.html", context)


@login_required
def fiche_patient_delete(request, id_fiche):
    # dictionary for initial data with
    # field names as keys
    context = {}

    fiche_patient = get_object_or_404(FichePatient, id_fiche=id_fiche)

    if request.method == "POST":

        fiche_patient.delete()

        return redirect("patient_list")

    return render(request, "pages/doctor/fiche_patient_delete.html", context)


@login_required()
def fichePDF(request, id_fiche):
    fiche_patient = get_object_or_404(FichePatient, id_fiche=id_fiche)

    template_path = 'pages/doctor/fiche_pdf.html'

    context = {'fiche_patient': fiche_patient}

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="dossier medicale de patient.pdf"'

    template = get_template(template_path)

    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


class OrdonnanceForm(forms.ModelForm):
    class Meta:
        model = Ordonnance
        fields = ['name_patient', 'date', 'medicament', 'observation']


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


@login_required()
def rdv_annuelle(request):

    return render(request, "pages/doctor/rdv_annuelle.html")


@login_required()
def rdv_annuellle(request):

    return render(request, "pages/ESI/rdv_annuellle.html")


@login_required()
def ViewPDF(request, id_ordonnance):
    ordonnance = get_object_or_404(Ordonnance, id_ordonnance=id_ordonnance)

    template_path = 'pages/doctor/pdf_template.html'

    context = {'ordonnance': ordonnance}

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="ordonnance.pdf"'

    template = get_template(template_path)

    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['id_consultation', 'id_patient', 'contenue',
                  'antecedant', 'traitement', 'date_consultation']


@login_required()
def consultation_list(request, template_name='pages/doctor/consultation_list.html'):
    consultation = Consultation.objects.all()
    return render(request, template_name, {'consultation': consultation})


@login_required()
def consultation(request, template_name='pages/doctor/consultation.html'):
    form = ConsultationForm(request.POST or None)

    if form.is_valid():
        consultation = form.save(commit=False)
        consultation.save()
        return redirect('consultation_list')
    return render(request, template_name, {'form': form})


@login_required()
def consultation_edit(request, id_consultation):
    # dictionary for initial data with
    # field names as keys
    context = {}

    consultation = get_object_or_404(
        Consultation, id_consultation=id_consultation)

    form = ConsultationForm(request.POST or None, instance=consultation)

    if form.is_valid():

        form.save()
        return redirect("consultation_list")

    context["form"] = form

    return render(request, "pages/doctor/consultation.html", context)


@login_required
def consultation_delete(request, id_consultation):
    # dictionary for initial data with
    # field names as keys
    context = {}

    consultation = get_object_or_404(
        Consultation, id_consultation=id_consultation)

    if request.method == "POST":

        consultation.delete()

        return redirect("consultation_list")

    return render(request, "pages/doctor/consultation_delete.html", context)


@login_required()
def Data(request):
    if request.user.groups.filter(name='ESI'):
        dataa = Consultation.objects.values(
            'antecedant').annotate(count=Count('id_consultation'))
        data = Consultation.objects.values('antecedant').distinct
        return render(request, 'pages/ESI/statistics.html', {'data': data, 'dataa': dataa})
    elif request.user.groups.filter(name='doctor'):
        dataa = Consultation.objects.values(
            'antecedant').annotate(count=Count('id_consultation'))
        data = Consultation.objects.values('antecedant').distinct
        if request.method == 'POST':
            form = DataFrom(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/doctor/Statistique')
        else:
            form = DataFrom()
        context = {
            'data': data,
            'dataa': dataa,

            'form': form,
        }
        return render(request, 'pages/doctor/statistics.html', context)


def rd(request):
    current_user = request.user
    rdv = Rdv.objects.filter(id_patient=current_user.id)
    return render(request, 'pages/patient/patient_rdv.html', {'rdv': rdv})


class RdForm(forms.ModelForm):
    class Meta:
        model = Rdv
        fields = ['date', 'num_rdv']
        widgets = {
            'date': forms.TextInput(attrs={'class': 'w3-input w3-border w3-round', }),
            'num_rdv': forms.NumberInput(attrs={'class': 'w3-input w3-border w3-round', }),
        }


@login_required
def rd_create(request, template_name='pages/patient/rd_form.html'):
    form = RdForm(request.POST or None)

    if form.is_valid():
        rdv = form.save(commit=False)
        rdv.id_patient = request.user
        rdv.num_rdv = CountNumeroRdv()
        rdv.save()
        return redirect('rd')
    return render(request, template_name, {'form': form})


@login_required
def rd_update(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    rdv = get_object_or_404(Rdv, id=id)

    form = RdvForm(request.POST or None, instance=rdv)

    if form.is_valid():
        rdv.id_patient = request.user
        form.save()
        return redirect("rd")

    context["form"] = form

    return render(request, "pages/patient/rd_form.html", context)


@login_required
def rd_delete(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    rdv = get_object_or_404(Rdv, id=id)

    if request.method == "POST":
        rdv.id_patient = request.user
        rdv.delete()
        rdv.num_rdv = CountNumeroRdv()

        return redirect("rd")

    return render(request, "pages/patient/rd_confirm_delete.html", context)


def consultation_list_patient(request, template_name='pages/patient/consultation_list_patient.html'):
    current_user = request.user
    consultation = Consultation.objects.filter(id_patient=current_user.id)
    return render(request, template_name, {'consultation': consultation})
