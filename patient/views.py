from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import EditProfileForm


# patient/views.


def patient(request):
    if request.user.groups.filter(name="Patients"):
        return render(request, "pages/patient/patient_dashboard.html")
    else:
        # messages.info(request, '')
        return redirect("../login")


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
