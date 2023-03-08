from django.db import models
from django.contrib.auth.models import User


departments = [
    ("Cardiologist", "Cardiologist"),
    ("Generalist", "Generalist"),
    ("Dermatologists", "Dermatologists"),
    ("Emergency Medicine Specialists", "Emergency Medicine Specialists"),
    ("Allergists/Immunologists", "Allergists/Immunologists"),
    ("Anesthesiologists", "Anesthesiologists"),
    ("Colon and Rectal Surgeons", "Colon and Rectal Surgeons"),
]
# ----------------------------------------------------------------------------
# ---------------------------- Doctor model ----------------------------------
# ----------------------------------------------------------------------------
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to="profile_pic/DoctorProfilePic/", null=True, blank=True
    )
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=True)
    department = models.CharField(
        max_length=50, choices=departments, default="Generalist"
    )
    status = models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return "{} ({})".format(self.user.first_name, self.department)


class Consultation(models.Model):
    doctorId = models.ForeignKey(
        Doctor,
        related_name="conssultation_doctor",
        on_delete=models.CASCADE,
    )
    patientId = models.ForeignKey(
        "patient.Patient",
        related_name="consultation_patient",
        on_delete=models.CASCADE,
    )
    consultationDate = models.DateTimeField()
    notes = models.TextField(max_length=254)
    diagnosis = models.TextField()
    treatment = models.TextField()

    def __str__(self):
        return str(self.patientId.username)


""" class Facture(models.Model):
    id_facture = models.AutoField(primary_key=True)
    # id_consultation = models.ForeignKey('Consultation',related_name="facture_consultation",on_delete=models.CASCADE, )
    prix = models.FloatField()
    date = models.DateTimeField()

    def __str__(self):
        return str(self.date) """
