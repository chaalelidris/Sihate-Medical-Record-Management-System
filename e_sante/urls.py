from django.urls import path
from . import views

urlpatterns = [
    path("doctor/", views.doctor, name='doctor'),
    path("patient/", views.patient, name='patient'),
    path("logout/", views.logout, name="logout"),
    path("rendez-vous", views.rdv_list, name='rdv_list'),
    path("new", views.rdv_create, name='rdv_new'),
    path("edit/(?P<id>\d+)", views.rdv_update, name='rdv_edit'),
    path("delete/(?P<id>\d+)", views.rdv_delete, name='rdv_delete'),
    path("patient_list", views.patient_list, name='patient_list'),
    path("ordonnance", views.ordonnance, name='ordonnance'),
    path("ordonnance_list", views.ordonnance_list, name='ordonnance_list'),
    path("ordonnance_edit/(?P<id_ordonnance>\d+)", views.ordonnance_edit, name='ordonnance_edit'),
    path("ordonnance_delete/(?P<id_ordonnance>\d+)", views.ordonnance_delete, name='ordonnance_delete'),

]
