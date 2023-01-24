from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


class OrdonnanceForm(forms.ModelForm):
    class Meta:
        model = Ordonnance
        fields = ["name_patient", "date", "medicament", "observation"]


def ordonnance_list(request, template_name="pages/doctor/ordonnance_list.html"):
    ordonnance = Ordonnance.objects.all()
    return render(request, template_name, {"ordonnance": ordonnance})


def ordonnance(request, template_name="pages/doctor/ordonnance.html"):
    form = OrdonnanceForm(request.POST or None)

    if form.is_valid():
        ordonnance = form.save(commit=False)
        ordonnance.save()
        return redirect("ordonnance_list")
    return render(request, template_name, {"form": form})


def ordonnance_edit(request, id_ordonnance):
    # dictionary for initial data with
    # field names as keys
    context = {}

    ordonnance = get_object_or_404(Ordonnance, id_ordonnance=id_ordonnance)

    form = OrdonnanceForm(request.POST or None, instance=ordonnance)

    if form.is_valid():

        form.save()
        return redirect("ordonnance_list")

    context["form"] = form

    return render(request, "pages/doctor/ordonnance.html", context)


@login_required
def ordonnance_delete(request, id_ordonnance):
    # dictionary for initial data with
    # field names as keys
    context = {}

    ordonnance = get_object_or_404(Ordonnance, id_ordonnance=id_ordonnance)

    if request.method == "POST":

        ordonnance.delete()

        return redirect("ordonnance_list")

    return render(request, "pages/doctor/ordonnance_delete.html", context)
