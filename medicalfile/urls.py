from django.urls import path, include
from . import views

urlpatterns = [
    path(
        "fiche_patient_edit/<int:id_fiche>/",
        views.fiche_patient_edit,
        name="fiche_patient_edit",
    ),
    path(
        "fiche_patient_delete/<int:id_fiche>/",
        views.fiche_patient_delete,
        name="fiche_patient_delete",
    ),
    path("fichePDF/<int:id_fiche>/", views.fichePDF, name="fichePDF"),
]
