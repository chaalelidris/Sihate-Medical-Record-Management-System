from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .. import forms, models


# ---------------------------------------------------------------------------------------------
# ----------------- OfficeManager views -------------------------------------------------------
# ---------------------------------------------------------------------------------------------


@user_passes_test(lambda u: u.is_authenticated and u.is_manager)
def manager_dashboard_view(request):
    manager = models.OfficeManager.objects.get(id=request.user.id)
    patients = models.Patient.objects.order_by("-id")[:5]
    doctors = models.Doctor.objects.order_by("-id")[:5]

    messages.success(request, "Welcome manager")

    context = {
        "manager": manager,
        "doctors": doctors,
        "patients": patients,
        "segment": "dashboard",
    }
    return render(request, "profiles/manager/dashboard/manager_dashboard.html", context)


# PROFILE VIEW
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


# PATIENTS VIEW
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


# DOCTORS VIEW
@user_passes_test(lambda u: u.is_authenticated and u.is_manager)
def manager_doctors_view(request):
    manager = models.OfficeManager.objects.get(id=request.user.id)
    doctors = models.Doctor.objects.all()

    context = {
        "manager": manager,
        "doctors": doctors,
        "segment": "doctors",
    }
    return render(request, "profiles/manager/doctors/manager_doctors.html", context)
