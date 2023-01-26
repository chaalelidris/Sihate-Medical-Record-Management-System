from django.urls import path, include
from . import views

urlpatterns = [
    path(
        "prescription_pdf/<int:id_ordonnance>/",
        views.prescription_pdf,
        name="prescription_pdf",
    ),
    path("", views.prescription, name="prescription"),
    path("prescription_list/", views.prescription_list, name="prescription_list"),
    path(
        "prescription_edit/<int:id_ordonnance>/",
        views.prescription_edit,
        name="prescription_edit",
    ),
    path(
        "prescription_delete/<int:id_ordonnance>/",
        views.prescription_delete,
        name="prescription_delete",
    ),
]
