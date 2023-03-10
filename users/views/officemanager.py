from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .. import forms, models


# ---------------------------------------------------------------------------------------------
# ----------------- OfficeManager views -------------------------------------------------------
# ---------------------------------------------------------------------------------------------


@user_passes_test(lambda u: u.is_authenticated and u.is_officemanager)
def office_manager_view(request):
    if request.user.groups.filter(name="office_manager"):
        return render(request, "pages/medical_office/medical_office_dashboard.html")
    else:
        # messages.info(request, '')
        return redirect("login")


@user_passes_test(lambda u: u.is_authenticated and u.is_officemanager)
def office_manager_profile_view(request):
    return render(request, "pages/medical_office/medical_office_dashboard.html")


@user_passes_test(lambda u: u.is_authenticated and u.is_officemanager)
def statistics_view(request):
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


# ---------------------------------------------------------------------------------------------
# ------------------------------------------------------- **End OfficeManager** ---------------
# ---------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------
# ----------------- Users registration views --------------------------------------------------
# ---------------------------------------------------------------------------------------------
@user_passes_test(lambda u: u.is_authenticated and u.is_officemanager)
def doctor_signup_view(request):
    if request.method == "POST":
        form = DoctorSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_doctor = True
            user.save()
            doctor = Doctor.objects.create(
                user=user, specialty=form.cleaned_data["specialty"]
            )
            doctor.save()
            return redirect("doctor_view")
    else:
        form = DoctorSignupForm()
    return render(request, "doctor_signup.html", {"form": form})


@user_passes_test(lambda u: u.is_authenticated and u.is_officemanager)
def patient_signup_view(request):
    if request.method == "POST":
        form = PatientSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_officemanager = True
            user.save()
            patient = Patient.objects.create(user=user, age=form.cleaned_data["age"])
            patient.save()
            return redirect("patient_view")
    else:
        form = PatientSignupForm()
    return render(request, "patient_signup.html", {"form": form})


@user_passes_test(lambda u: u.is_authenticated and u.is_officemanager)
def officemanager_signup_view(request):
    if request.method == "POST":
        form = OfficeManagerSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_officemanager = True
            user.save()
            officemanager = OfficeManager.objects.create(
                user=user, phone_number=form.cleaned_data["phone_number"]
            )
            officemanager.save()
            return redirect("officemanager_view")
    else:
        form = OfficeManagerSignupForm()
    return render(request, "officemanager_signup.html", {"form": form})
