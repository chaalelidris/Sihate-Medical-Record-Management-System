from django import forms
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from django.shortcuts import render
from xhtml2pdf import pisa


def patient_profile(request):
    user = request.user
    form = EditProfileForm(request.POST or None, instance=user)
    if request.method == "POST":
        if form.is_valid():

            form.save()

            new_password = form.cleaned_data.get("password")
            if new_password:
                user.set_password(new_password)
                form.save(new_password)

            return HttpResponseRedirect(reverse("patient"))

    context = {"form": form}

    return render(request, "pages/patient/patient_profile.html", context)


def patient(request):
    if request.user.groups.filter(name="Patients"):
        return render(request, "pages/patient/patient_dashboard.html")
    else:
        # messages.info(request, '')
        return redirect("../login")


def logout(request):
    auth.logout(request)
    # return redirect("../login")


@login_required()
def Data(request):
    if request.user.groups.filter(name="ESI"):
        dataa = Consultation.objects.values("antecedant").annotate(
            count=Count("id_consultation")
        )
        data = Consultation.objects.values("antecedant").distinct
        return render(
            request, "pages/ESI/statistics.html", {"data": data, "dataa": dataa}
        )
    elif request.user.groups.filter(name="doctor"):
        dataa = Consultation.objects.values("antecedant").annotate(
            count=Count("id_consultation")
        )
        data = Consultation.objects.values("antecedant").distinct
        if request.method == "POST":
            form = DataFrom(request.POST)
            if form.is_valid():
                form.save()
                return redirect("/doctor/Statistique")
        else:
            form = DataFrom()
        context = {
            "data": data,
            "dataa": dataa,
            "form": form,
        }
        return render(request, "pages/doctor/statistics.html", context)


def rd(request):
    current_user = request.user
    rdv = Rdv.objects.filter(id_patient=current_user.id)
    return render(request, "pages/patient/patient_rdv.html", {"rdv": rdv})


@login_required
def rd_create(request, template_name="pages/patient/rd_form.html"):
    form = RdForm(request.POST or None)

    if form.is_valid():
        rdv = form.save(commit=False)
        rdv.id_patient = request.user
        rdv.num_rdv = CountNumeroRdv()
        rdv.save()
        return redirect("rd")
    return render(
        request,
        template_name,
    )


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


def consultation_list_patient(
    request, template_name="pages/patient/consultation_list_patient.html"
):
    current_user = request.user
    consultation = Consultation.objects.filter(id_patient=current_user.id)
    return render(request, template_name, {"consultation": consultation})
