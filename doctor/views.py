from django import forms
from django.db.models import Count
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Consultation

# Doctor views.


def doctor(request):

    if request.user.groups.filter(name="doctor"):
        return render(request, "pages/doctor/doctor_dashboard.html")
    else:
        # messages.info(request, '')
        return redirect("../login")


def doctor_profile(request):

    user = request.user
    # edit profile

    if request.method == "POST":
        pass

    return render(
        request,
        "pages/doctor/doctor_profile.html",
    )


def prescription_pdf():
    pass


def patient_list(request, template_name="pages/doctor/patient_list.html"):
    fiche_patient = FichePatient.objects.all()
    return render(request, template_name, {"fiche_patient": fiche_patient})


def consultation_list_patient(
    request, template_name="pages/patient/consultation_list_patient.html"
):
    current_user = request.user
    consultation = Consultation.objects.filter(id_patient=current_user.id)
    return render(request, template_name, {"consultation": consultation})


@login_required()
def consultation_list(request, template_name="pages/doctor/consultation_list.html"):
    consultation = Consultation.objects.all()
    return render(request, template_name, {"consultation": consultation})


@login_required()
def consultation(request, template_name="pages/doctor/consultation.html"):
    form = ConsultationForm(request.POST or None)

    if form.is_valid():
        consultation = form.save(commit=False)
        consultation.save()
        return redirect("consultation_list")
    return render(request, template_name, {"form": form})


@login_required()
def consultation_edit(request, id_consultation):
    # dictionary for initial data with
    # field names as keys
    context = {}

    consultation = get_object_or_404(Consultation, id_consultation=id_consultation)

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

    consultation = get_object_or_404(Consultation, id_consultation=id_consultation)

    if request.method == "POST":

        consultation.delete()

        return redirect("consultation_list")

    return render(request, "pages/doctor/consultation_delete.html", context)


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
