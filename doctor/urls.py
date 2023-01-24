from django.urls import path, include
from . import views

urlpatterns = [
    path("profile/", views.doctor_profile, name="doctor_profile"),
    path("view_pdf/<int:id_ordonnance>/", views.view_pdf, name="view_pdf"),
    path("patient_list", views.patient_list, name="patient_list"),
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
    path("ordonnance/", views.ordonnance, name="ordonnance"),
    path("ordonnance_list/", views.ordonnance_list, name="ordonnance_list"),
    path(
        "ordonnance_edit/<int:id_ordonnance>/",
        views.ordonnance_edit,
        name="ordonnance_edit",
    ),
    path(
        "ordonnance_delete/<int:id_ordonnance>/",
        views.ordonnance_delete,
        name="ordonnance_delete",
    ),
    path("consultation_list/", views.consultation_list, name="consultation_list"),
    path(
        "consultation_list_patient/",
        views.consultation_list_patient,
        name="consultation_list_patient",
    ),
    path("consultation/", views.consultation, name="consultation"),
    path(
        "consultation_edit/<int:id_consultation>/",
        views.consultation_edit,
        name="consultation_edit",
    ),
    path(
        "consultation_delete/<int:id_consultation>/",
        views.consultation_delete,
        name="consultation_delete",
    ),
    path("statistique/", views.Data, name="Data"),
]
