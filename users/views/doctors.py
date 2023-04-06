from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .. import forms, models
from medical_records.models import MedicalRecord


# ---------------------------------------------------------------------------------------------
# --------------------------------------- Doctor views ----------------------------------------
# ---------------------------------------------------------------------------------------------


@user_passes_test(lambda u: u.is_authenticated and u.is_doctor)
def doctor_view(request):
    doctor = models.Doctor.objects.get(id=request.user.id)

    context = {"doctor": doctor}
    return render(
        request, "profiles/users/doctor/dashboard/doctor_dashboard.html", context
    )

@user_passes_test(lambda u: u.is_authenticated and u.is_doctor)
def doctor_profile_view(request, pk):

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

    return render(request, "profiles/users/doctor/doctor_profile.html", context=mydict)


@user_passes_test(lambda u: u.is_authenticated and u.is_doctor)
def patient_list_view(request):
    patient_medical_file = MedicalRecord.objects.all()
    return render(
        request,
        "profiles/users/doctor/patient/patient_list.html",
        {"patient_medical_file": patient_medical_file},
    )


@user_passes_test(lambda u: u.is_authenticated and u.is_doctor)
def patient_details_view(request):
    patient = Patient.objects.all()
    return render(
        request,
        "profiles/users/doctor/patient/patient.html",
        {"patient_medical_file": patient},
    )


@user_passes_test(lambda u: u.is_authenticated and u.is_doctor)
def consultation_list_view(request):
    consultation = Consultation.objects.all()
    return render(
        request,
        "profiles/users/doctor/consultation/consultation_list.html",
        {"consultation": consultation},
    )


@user_passes_test(lambda u: u.is_authenticated and u.is_doctor)
def consultation_view(
    request, template_name="profiles/users/doctor/consultation/consultation.html"
):
    form = ConsultationForm(request.POST or None)

    if form.is_valid():
        consultation = form.save(commit=False)
        consultation.save()
        return redirect("consultation_list")
    return render(request, template_name, {"form": form})


@user_passes_test(lambda u: u.is_authenticated and u.is_doctor)
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

    return render(
        request, "profiles/users/doctor/consultaion/consultation.html", context
    )


@user_passes_test(lambda u: u.is_authenticated and u.is_doctor)
def delete_consultation_view(request, id_consultation):
    # dictionary for initial data with
    # field names as keys
    context = {}

    consultation = get_object_or_404(Consultation, id_consultation=id_consultation)

    if request.method == "POST":

        consultation.delete()

        return redirect("consultation_list")

    return render(
        request, "profiles/users/doctor/consultation/consultation_delete.html", context
    )


@user_passes_test(lambda u: u.is_authenticated and u.is_doctor)
def statistics_view(request):
    if request.user.groups.filter(name="medical_office"):
        statistics = Consultation.objects.values("diagnosis").annotate(
            count=Count("id_consultation")
        )
        data = Consultation.objects.values("diagnosis").distinct
        return render(
            request,
            "medical_office/statistics.html",
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
        return render(
            request, "profiles/users/doctor/statistics/statistics.html", context
        )


# ---------------------------------------------------------------------------------------------
# -------------------------------------------------------**End Doctor views** -----------------
# ---------------------------------------------------------------------------------------------
