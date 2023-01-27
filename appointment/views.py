from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Appointment
from .forms import PostForm, AppointmentForm

# Create your views here.
@login_required
def create_appointment(request, template_name="pages/doctor/appointment_form.html"):
    form = AppointmentForm(request.POST or None)

    if form.is_valid():
        appointment = form.save(commit=False)
        appointment.num_appointment = countAppointment()
        appointment.save()
        return redirect("appointment_list")
    return render(request, template_name, {"form": form})


@login_required
def appointment_list(request):
    appointment = Appointment.objects.all()
    return render(
        request, "pages/doctor/appointment_list.html", {"appointment": appointment}
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

    return render(request, "pages/doctor/appointment_form.html", context)


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

    return render(request, "pages/doctor/appointment_confirm_delete.html", context)


@login_required()
def yearly_appointment(request):
    return render(request, "pages/doctor/appointment_annuelle.html")


def countAppointment():
    no = Appointment.objects.count()
    if no == None:
        return 1
    else:
        return no + 1


def newAppointment(request):
    form = PostForm(request.POST)

    if form.is_valid():
        appointment = form.save(commit=False)
        appointment.id_patient = request.user.id
        appointment.id_medecin = 1
        appointment.num_appointment = 1
        # WE NEED ID_PATIENT + ID_SEC + NUMERORDV IS STATIC PROBLEM
        appointment.save()
    context = {
        "form": form,
    }

    return render(request, "pages/doctor/appointment_form", context)


def appointment(request):
    current_user = request.user
    appointment = Appointment.objects.filter(id_patient=current_user.id)
    return render(
        request, "pages/patient/patient_rdv.html", {"appointment": appointment}
    )


@login_required
def rd_create(request, template_name="pages/patient/rd_form.html"):
    form = AppointmentForm(request.POST or None)

    if form.is_valid():
        rdv = form.save(commit=False)
        rdv.id_patient = request.user
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
        appointment.id_patient = request.user
        form.save()
        return redirect("rd")

    context["form"] = form

    return render(request, "pages/patient/rd_form.html", context)


@login_required
def rd_delete(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    rdv = get_object_or_404(Appointment, id=id)

    if request.method == "POST":
        rdv.id_patient = request.user
        rdv.delete()
        rdv.num_rdv = countAppointment()

        return redirect("rd")

    return render(request, "pages/patient/rd_confirm_delete.html", context)