from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Appointment
from .forms import AppointmentForm

# Create your views here.
@login_required
def create_appointment(request):

    if request.POST:
        form = AppointmentForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect("appointment_list")

    return render(
        request,
        "profiles/users/doctor/appointment/appointment_form.html",
        {"form": form},
    )


@login_required
def appointment_list(request):
    appointment = Appointment.objects.all()
    return render(
        request,
        "profiles/users/doctor/appointment/appointment_list.html",
        {"appointment": appointment},
    )


@login_required
def edit_appointment(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    appointment = get_object_or_404(Appointment, id=id)

    form = AppointmentForm(request.POST or None, instance=appointment)

    if form.is_valid():

        form.save()
        return redirect("appointment_list")

    context["form"] = form

    return render(
        request, "profiles/users/doctor/appointment/appointment_form.html", context
    )


@login_required
def delete_appointment(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    appointment = get_object_or_404(Appointment, id=id)

    if request.method == "POST":

        appointment.delete()
        appointment.num_appointment = countAppointment()

        return redirect("appointment_list")

    return render(
        request,
        "profiles/users/doctor/appointment/appointment_confirm_delete.html",
        context,
    )


@login_required()
def yearly_appointment(request):
    return render(request, "profiles/users/doctor/appointment/yearly_appointment.html")


def countAppointment():
    no = Appointment.objects.count()
    if no == None:
        return 1
    else:
        return no + 1


def appointment(request):
    current_user = request.user
    appointment = Appointment.objects.filter(patient_id=current_user.id)
    return render(
        request, "patient/patient_rdv.html", {"appointment": appointment}
    )


@login_required
def rd_create(request, template_name="patient/rd_form.html"):
    form = AppointmentForm(request.POST or None)

    if form.is_valid():
        rdv = form.save(commit=False)
        rdv.patient_id = request.user
        rdv.num_rdv = countAppointment()
        rdv.save()
        return redirect("rd")
    return render(
        request,
        template_name,
    )


@login_required
def rd_update(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    appointment = get_object_or_404(Appointment, id=id)

    form = AppointmentForm(request.POST or None, instance=appointment)

    if form.is_valid():
        appointment.patient_id = request.user
        form.save()
        return redirect("rd")

    context["form"] = form

    return render(request, "patient/rd_form.html", context)


@login_required
def rd_delete(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    rdv = get_object_or_404(Appointment, id=id)

    if request.method == "POST":
        rdv.patient_id = request.user
        rdv.delete()
        rdv.num_rdv = countAppointment()

        return redirect("rd")

    return render(request, "patient/rd_confirm_delete.html", context)
