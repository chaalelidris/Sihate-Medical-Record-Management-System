from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

from django.views.generic.base import TemplateView

from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import redirect, render

from .forms import ContactusForm
from users import forms as users_forms, models as users_models

# -------------------------------------------------------------------------------
# -------------for checking user is doctor , patient or admin(by sumit)----------
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# ------------------------ Home view and Contact Form ---------------------------
# -------------------------------------------------------------------------------


# -------------------------------- User Login  ----------------------------------
# -------------------------------------------------------------------------------
def home_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    if users_models.Doctor.objects.filter(username=username).exists():
                        login(request, user)
                        messages.success(request, "Welcome doctor ")
                        return redirect("doctor_view")

                    elif users_models.Patient.objects.filter(
                        username=username
                    ).exists():
                        login(request, user)
                        messages.success(request, "Welcome patient ")
                        return redirect("patient_view")

                    elif users_models.OfficeManager.objects.filter(
                        username=username
                    ).exists():
                        login(request, user)
                        messages.success(request, "Welcome office manager ")
                        return redirect("officemanager_view")

                else:
                    messages.error(request, "User unknown please contact admin !")

            else:
                messages.error(request, "Invalid username or password.")

        else:
            messages.error(request, "Invalid username or password.")

    else:
        form = AuthenticationForm()
    return render(request, "index/index.html", {"form": form})


# -------------------------------------------------------------------------------
# -------------------------------- User Signup  ---------------------------------
# -------------------------------------------------------------------------------


def doctor_signup_view(request):
    if request.method == "POST":
        form = users_forms.DoctorSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_doctor = True
            user.save()
            messages.success(request, f"Account created for {user.username}!")
            return redirect("doctor_view")
    else:
        form = users_forms.DoctorSignupForm()
    context = {"form": form}

    return render(request, "index/register/doctor_signup.html", context)


def patient_signup_view(request):
    if request.method == "POST":
        form = users_forms.PatientSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_patient = True
            user.save()
            messages.success(request, f"Account created for {user.username}!")
            return redirect("patient_view")
    else:
        form = users_forms.PatientSignupForm()
    return render(request, "index/register/patient_signup.html", {"form": form})


def officemanager_signup_view(request):
    if request.method == "POST":
        form = users_forms.OfficeManagerSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_officemanager = True
            user.save()
            officemanager = OfficeManager.objects.create(
                user=user, mobile=form.cleaned_data["phone_number"]
            )
            officemanager.save()
            return redirect("officemanager_view")
    else:
        form = users_forms.OfficeManagerSignupForm()
    return render(request, "pages\register\officemanager_signup.html", {"form": form})
