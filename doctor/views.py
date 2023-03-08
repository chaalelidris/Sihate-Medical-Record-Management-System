from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import forms, models
from medicalrecord.models import MedicalRecord

# Doctor views.


def doctorDashboardView(request):
    if request.user.groups.filter(name="doctor"):
        return render(request, "pages/doctor/doctor_dashboard.html")
    else:
        # messages.info(request, '')
        return redirect("../login")


def updateProfileView(request, pk):

    doctor = models.Doctor.objects.get(id=pk)
    user = models.User.objects.get(id=doctor.user_id)

    userForm = forms.DoctorUserForm(instance=user)
    doctorForm = forms.DoctorForm(request.FILES, instance=doctor)
    mydict = {"userForm": userForm, "doctorForm": doctorForm}
    if request.method == "POST":
        userForm = forms.DoctorUserForm(request.POST, instance=user)
        doctorForm = forms.DoctorForm(request.POST, request.FILES, instance=doctor)
        if userForm.is_valid() and doctorForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            doctor = doctorForm.save(commit=False)
            doctor.status = True
            doctor.save()
            return redirect("doctor_profile")

    return render(request, "pages/doctor/doctor_profile.html", context=mydict)


def prescription_pdf():
    pass


def patientListView(request):
    patient_medical_file = MedicalRecord.objects.all()
    return render(
        request,
        "pages/doctor/patient/patient_list.html",
        {"patient_medical_file": patient_medical_file},
    )


def consultation_list_patient(
    request, template_name="pages/patient/consultation_list_patient.html"
):
    current_user = request.user
    consultation = Consultation.objects.filter(patientId=current_user.id)
    return render(request, template_name, {"consultation": consultation})


@login_required()
def consultation_list(request):
    consultation = Consultation.objects.all()
    return render(
        request,
        "pages/doctor/consultation/consultation_list.html",
        {"consultation": consultation},
    )


@login_required()
def consultation(request, template_name="pages/doctor/consultation/consultation.html"):
    form = ConsultationForm(request.POST or None)

    if form.is_valid():
        consultation = form.save(commit=False)
        consultation.save()
        return redirect("consultation_list")
    return render(request, template_name, {"form": form})


@login_required()
def updateConsultationView(request, id_consultation):
    # dictionary for initial data with
    # field names as keys
    context = {}

    consultation = get_object_or_404(Consultation, id_consultation=id_consultation)

    form = ConsultationForm(request.POST or None, instance=consultation)

    if form.is_valid():

        form.save()
        return redirect("consultation_list")

    context["form"] = form

    return render(request, "pages/doctor/consultaion/consultation.html", context)


@login_required
def deleteConsultationView(request, id_consultation):
    # dictionary for initial data with
    # field names as keys
    context = {}

    consultation = get_object_or_404(Consultation, id_consultation=id_consultation)

    if request.method == "POST":

        consultation.delete()

        return redirect("consultation_list")

    return render(
        request, "pages/doctor/consultation/consultation_delete.html", context
    )


@login_required()
def Data(request):
    if request.user.groups.filter(name="medical_office"):
        statistics = Consultation.objects.values("diagnosis").annotate(
            count=Count("id_consultation")
        )
        data = Consultation.objects.values("diagnosis").distinct
        return render(
            request,
            "pages/medical_office/statistics.html",
            {"data": data, "statistics": statistics},
        )
    elif request.user.groups.filter(name="doctor"):
        statistics = Consultation.objects.values("diagnosis").annotate(
            count=Count("id_consultation")
        )
        data = Consultation.objects.values("diagnosis").distinct
        if request.method == "POST":
            form = ConsultationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("/doctor/statistique")
        else:
            form = ConsultationForm()
        context = {
            "data": data,
            "statistics": statistics,
            "form": form,
        }
        return render(request, "pages/doctor/statistics/statistics.html", context)
