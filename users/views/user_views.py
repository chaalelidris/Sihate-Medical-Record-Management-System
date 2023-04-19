from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

from django.conf import settings
from django.shortcuts import redirect, render

from .. import forms, models as users_models

# -------------------------------------------------------------------------------
# -------------------------------- Redirect user  -------------------------------
# -------------------------------------------------------------------------------

# -----------for checking user is doctor , patient or manager
def is_patient(user):
    return user.is_patient


def is_doctor(user):
    return user.is_doctor


def is_manager(user):
    return user.is_manager


# ----------- USER WAITING VIEW
def user_waiting_view(request, template_name):
    return render(request, template_name)


# ---------AFTER ENTERING CREDENTIALS WE CHECK WHETHER USERNAME AND PASSWORD IS OF ADMIN,DOCTOR OR PATIENT
def user_view(request, user):
    if is_doctor(user):
        doctor = users_models.Doctor.objects.get(id=user.id)
        if doctor.status:
            login(request, user)
            return redirect("doctor_dashboard_view")
        else:
            return redirect("user_waiting_view")

    elif is_patient(user):
        patient = users_models.Patient.objects.get(id=user.id)
        if patient.status:
            login(request, user)
            return redirect("patient_dashboard_view")
        else:
            return user_waiting_view(request, "profiles/patient/waiting/waiting.html")

    elif is_manager(user):
        login(request, user)
        return redirect("manager_dashboard_view")


# -------------------------------------------------------------------------------
# -------------------------------- User Login  ----------------------------------
# -------------------------------------------------------------------------------


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    return user_view(request, user)

                else:
                    messages.error(request, "User unknown please contact admin !")

            else:
                messages.error(request, "Invalid username or password.")

        else:
            messages.error(request, "Invalid username or password.")

    else:
        form = AuthenticationForm()
    return render(request, "index/login/login.html", {"form": form})


# -------------------------------------------------------------------------------
# -------------------------------- User Signup  ---------------------------------
# -------------------------------------------------------------------------------


def doctor_signup_view(request):
    if request.method == "POST":
        form = forms.DoctorSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_doctor = True
            user.save()
            messages.success(request, f"Account created for {user.username}!")
            return redirect("login_view")
    else:
        form = forms.DoctorSignupForm()
    context = {"form": form}

    return render(request, "index/register/doctor_signup.html", context)


def patient_signup_view(request):
    if request.method == "POST":
        form = forms.PatientSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_patient = True
            user.save()
            messages.success(request, f"Account created for {user.username}!")
            return redirect("login_view")
    else:
        form = forms.PatientSignupForm()
    return render(request, "index/register/patient_signup.html", {"form": form})


def manager_signup_view(request):
    if request.method == "POST":
        form = forms.OfficeManagerSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_manager = True
            user.save()
            return redirect("login_view")
    else:
        form = forms.OfficeManagerSignupForm()
    return render(request, "index/register/officemanager_signup.html", {"form": form})
