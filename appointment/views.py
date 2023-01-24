from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.


def newAppointment(request):
    form = PostForm(request.POST)

    if form.is_valid():
        rdv = form.save(commit=False)
        rdv.id_patient = request.user.id
        rdv.id_medecin = 1
        rdv.num_rdv = 1
        # WE NEED ID_PATIENT + ID_SEC + NUMERORDV IS STATIC PROBLEM
        rdv.save()
    context = {
        "form": form,
    }

    return render(request, "pages/doctor/rdv_form", context)


@login_required
def appointmentList(request):
    rdv = Rdv.objects.all()
    return render(request, "pages/doctor/rdv_list.html", {"rdv": rdv})


def countAppointment():
    no = Rdv.objects.count()
    if no == None:
        return 1
    else:
        return no + 1


@login_required
def createAppointment(request, template_name="pages/doctor/rdv_form.html"):
    form = RdvForm(request.POST or None)

    if form.is_valid():
        rdv = form.save(commit=False)
        rdv.num_rdv = CountNumeroRdv()
        rdv.save()
        return redirect("rdv_list")
    return render(request, template_name, {"form": form})


@login_required
def updateAppointment(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    rdv = get_object_or_404(Rdv, id=id)

    form = RdvForm(request.POST or None, instance=rdv)

    if form.is_valid():

        form.save()
        return redirect("rdv_list")

    context["form"] = form

    return render(request, "pages/doctor/rdv_form.html", context)


@login_required
def deleteAppointment(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    rdv = get_object_or_404(Rdv, id=id)

    if request.method == "POST":

        rdv.delete()
        rdv.num_rdv = CountNumeroRdv()

        return redirect("rdv_list")

    return render(request, "pages/doctor/rdv_confirm_delete.html", context)


@login_required()
def yearly_appointment(request):
    return render(request, "pages/doctor/rdv_annuelle.html")
