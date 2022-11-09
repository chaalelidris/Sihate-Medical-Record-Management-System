import json
from typing import NamedTuple
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.forms import forms
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import send_mail
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



def index(request):
    if request.method == "POST":
        Name = request.POST["Name"]
        Email = request.POST["Email"]
        Subject = request.POST["Subject"]
        Message = request.POST["Message"]

        # send email

        send_mail(
            Subject,  # subjetc
            Message,  # message
            Email,  # from
            ['guerzizines@gmail.com']  # to
        )

        messages.info(request, 'contact')
        return render(request, 'pages/index.html', {'Name': Name})
    else:
        return render(request, 'pages/index.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:

            if user.is_superuser:
                login(request, user)
                return redirect('../admin/')

            elif user.is_active:
                login(request, user)
                if request.user.groups.filter(name="doctor"):
                    return redirect('../doctor/')
                elif request.user.groups.filter(name="Patients"):
                    return redirect('../patient/')
                elif request.user.groups.filter(name="ESI"):
                    return redirect('../ESI/')
                else:
                    messages.info(request, 'User unknown')
                    return render(request, 'pages/login/login.html')

            else:
                messages.info(request, 'User unknown please contact admin !')
                return render(request, 'pages/login/login.html')

        else:
            messages.info(request, 'Username or Password is incorrect')
            return render(request, 'pages/login/login.html')
    else:
        return render(request, 'pages/login/login.html')
