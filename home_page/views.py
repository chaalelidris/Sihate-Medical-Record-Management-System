import json
from django.contrib.auth import authenticate, login
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib import messages

# from django.http import HttpResponse
def user_login_mobile(request):
    if request.method == "POST":
        body = json.loads(request.body)

        username = body.get("username", None)
        password = body.get("password", None)

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user:
                return HttpResponse(content="Logged in successfully", status=201)

        return HttpResponse(content="Creds doesn't exists", status=400)


class HomeView(TemplateView):
    template_name = "pages/index.html"

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        """ email = EmailMessage(
            subject=f"{name} from doctor family.",
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email],
        )

        email.send() """
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
