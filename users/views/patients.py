from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .. import forms, models


# ---------------------------------------------------------------------------------------------
# ----------------- Patient views -------------------------------------------------------------
# ---------------------------------------------------------------------------------------------


@user_passes_test(lambda u: u.is_authenticated and u.is_patient)
def patient_view(request):
    patient = models.Patient.objects.get(id=request.user.id)

    context = {"patient": patient}
    return render(
        request, "profiles/users/patient/dashboard/patient_dashboard.html", context
    )


@user_passes_test(lambda u: u.is_authenticated and u.is_patient)
def patient_profile_view(request):
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

    return render(request, "patient/patient_profile.html", context)


@user_passes_test(lambda u: u.is_authenticated and u.is_patient)
def consultation_list_patient(
    request, template_name="patient/consultation_list_patient.html"
):
    current_user = request.user
    consultation = Consultation.objects.filter(patient_id=current_user.id)
    return render(request, template_name, {"consultation": consultation})


# ---------------------------------------------------------------------------------------------
# -------------------------------------------------------**End Patient views** ----------------
# ---------------------------------------------------------------------------------------------
