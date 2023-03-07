from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import EditProfileForm
from django.http import HttpResponseRedirect

# Create your views here.


def medical_office(request):
    if request.user.groups.filter(name="medical_office"):
        return render(request, "pages/medical_office/medical_office_dashboard.html")
    else:
        # messages.info(request, '')
        return redirect("../login")


def medical_office_profile(request):
    user = request.user
    form = EditProfileForm(request.POST or None, instance=user)
    if request.method == "POST":
        if form.is_valid():

            form.save()

            new_password = form.cleaned_data.get("password")
            if new_password:
                user.set_password(new_password)
                form.save(new_password)

            return HttpResponseRedirect(reverse("medical_office"))

    context = {"form": form}

    return render(request, "pages/medical_office/medical_office_profile.html", context)
