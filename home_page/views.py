from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import ContactusForm


class homeView(TemplateView):
    template_name = "pages/index.html"

    def post(self, request):
        contactForm = ContactusForm()
        if request.method == "POST":
            contactForm = forms.ContactusForm(request.POST)
            if contactForm.is_valid():
                name = contactForm.cleaned_data["Name"]
                email = contactForm.cleaned_data["Email"]
                message = contactForm.cleaned_data["Message"]
                send_mail(
                    str(name) + " || " + str(email),
                    message,
                    settings.EMAIL_HOST_USER,
                    settings.EMAIL_RECEIVING_USER,
                    fail_silently=False,
                )
                return render(request, "hospital/contactussuccess.html")
        return render(request, "hospital/contactus.html", {"form": sub})

        return redirect("index")


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:

            if user.is_superuser:
                login(request, user)
                return redirect("../admin/")

            elif user.is_active:
                login(request, user)
                if request.user.groups.filter(name="doctor"):
                    return redirect("../doctor/")
                elif request.user.groups.filter(name="patient"):
                    return redirect("../patient/")
                elif request.user.groups.filter(name="office"):
                    return redirect("../medical_office/")
                else:
                    messages.info(request, "User unknown")
                    return render(request, "pages/login/login.html")

            else:
                messages.info(request, "User unknown please contact admin !")
                return render(request, "pages/login/login.html")

        else:
            messages.info(request, "Username or Password is incorrect")
            return render(request, "pages/login/login.html")
    else:
        return render(request, "pages/login/login.html")
