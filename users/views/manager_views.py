from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .. import forms, models
from appointment import models as appointment_models


# --------------------------------------------- Dashboard view -------------------------------------------------------


@user_passes_test(lambda u: u.is_authenticated and u.is_manager)
def manager_dashboard_view(request):
    manager = models.OfficeManager.objects.get(id=request.user.id)
    patients = models.Patient.objects.order_by("-id")[:5]
    doctors = models.Doctor.objects.order_by("-id")[:5]

    appointments_count = appointment_models.Appointment.objects.count()
    patients_count = models.Patient.objects.count()
    doctors_count = models.Doctor.objects.count()

    messages.success(request, "Welcome manager")

    context = {
        "manager": manager,
        "doctors": doctors,
        "patients": patients,
        "appointments_count": appointments_count,
        "patients_count": patients_count,
        "doctors_count": doctors_count,
        "segment": "dashboard",
    }
    return render(request, "profiles/manager/dashboard/manager_dashboard.html", context)


#
# ----------------------------------------- PROFILE VIEW ---------------------------------------------
#
@user_passes_test(lambda u: u.is_authenticated and u.is_manager)
def manager_profile_view(request):
    manager = models.OfficeManager.objects.get(id=request.user.id)

    if request.method == "POST":
        form = forms.ManagerUpdateForm(request.POST, request.FILES, instance=manager)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated!")
            return redirect("manager_profile_view")
        else:
            messages.error(
                request, "There was an error updating your profile. Please try again."
            )
    else:
        form = forms.ManagerUpdateForm(instance=manager)

    context = {
        "form": form,
        "manager": manager,
        "segment": "profile",
    }
    return render(request, "profiles/manager/profile/manager_profile.html", context)


#
# ----------------------------------------- PATIENTS VIEW ---------------------------------------------
#
@user_passes_test(lambda u: u.is_authenticated and u.is_manager)
def manager_patients_view(request):
    manager = models.OfficeManager.objects.get(id=request.user.id)
    patients = models.Patient.objects.all()

    if request.method == "POST":
        form = forms.PatientSignupForm(request.POST, request.FILES)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.is_patient = True
            patient.save()
            # Return success response with patient data
            return JsonResponse({"success": "Patient added successfully"})
        else:
            # Return error response with form errors
            return JsonResponse({"errors": form.errors})

    else:
        form = forms.PatientSignupForm()

    context = {
        "manager": manager,
        "patients": patients,
        "segment": "patients",
        "form": form,
    }
    return render(request, "profiles/manager/patients/manager_patients.html", context)


#
# ----------------------------------------- UPDATE PATIENT ---------------------------------------------
#
@user_passes_test(lambda u: u.is_authenticated and u.is_manager)
def manager_update_patient_view(request, pk):
    patient = get_object_or_404(models.Patient, pk=pk)

    if request.method == "POST":
        form = forms.PatientUpdateForm(request.POST, request.FILES, instance=patient)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": "Patient updated successfully"})
        else:
            # Return error response with form errors
            return JsonResponse({"errors": form.errors, "id": patient.id})
    else:
        form = forms.PatientUpdateForm(instance=patient)

    context = {
        "form": form,
        "patient": patient,
    }
    return render(request, "profiles/manager/patients/manager_patients.html", context)


# DELETE PATIENT
def manager_delete_patient_view(request, pk):
    patient = get_object_or_404(models.Patient, pk=pk)

    patient.delete()
    return redirect("manager_patients_view")


#
# ----------------------------------------- TOGGLE PATIENT STATUS ---------------------------------------------
#
@user_passes_test(lambda u: u.is_authenticated and u.is_manager)
def manager_patient_status_view(request, pk):
    patient = get_object_or_404(models.Patient, id=pk)

    if patient.status:
        patient.status = False
    else:
        patient.status = True

    patient.save()

    return redirect("manager_patients_view")


# ----------------------------------------------------------------------------------------------
# ---------------------------------------- DOCTORS VIEW ----------------------------------------
# ----------------------------------------------------------------------------------------------


@user_passes_test(lambda u: u.is_authenticated and u.is_manager)
def manager_doctors_view(request):
    manager = models.OfficeManager.objects.get(id=request.user.id)
    doctors = models.Doctor.objects.all()

    if request.method == "POST":
        form = forms.DoctorSignupForm(request.POST, request.FILES)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.is_doctor = True
            doctor.save()
            # Return success response with doctor data
            return JsonResponse({"success": "Doctor added successfully"})
        else:
            # Return error response with form errors
            return JsonResponse({"errors": form.errors})

    else:
        form = forms.DoctorSignupForm()

    context = {
        "manager": manager,
        "doctors": doctors,
        "segment": "doctors",
        "form": form,
    }
    return render(request, "profiles/manager/doctors/manager_doctors.html", context)


#
# ----------------------------------------- UPDATE DOCTOR ---------------------------------------------
#
@user_passes_test(lambda u: u.is_authenticated and u.is_manager)
def manager_update_doctor_view(request, pk):
    doctor = get_object_or_404(models.Doctor, pk=pk)

    if request.method == "POST":
        form = forms.DoctorUpdateForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": "Doctor updated successfully"})
        else:
            # Return error response with form errors
            return JsonResponse({"errors": form.errors, "id": doctor.id})
    else:
        form = forms.DoctorUpdateForm()(instance=doctor)

    context = {
        "form": form,
        "doctor": doctor,
    }
    return render(request, "profiles/manager/doctors/manager_patients.html", context)


# DELETE PATIENT
def manager_delete_doctor_view(request, pk):
    doctor = get_object_or_404(models.Doctor, pk=pk)

    doctor.delete()
    return redirect("manager_doctors_view")


#
# ----------------------------------------- TOGGLE DOCTOR STATUS ---------------------------------------------
#
@user_passes_test(lambda u: u.is_authenticated and u.is_manager)
def manager_doctor_status_view(request, pk):
    doctor = get_object_or_404(models.Doctor, id=pk)

    if doctor.status:
        doctor.status = False
    else:
        doctor.status = True

    doctor.save()

    return redirect("manager_doctors_view")
