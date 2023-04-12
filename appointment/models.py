from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# ----------------------------------------------------------------------------
# ---------------------------- Appointment model ----------------------------------
# ----------------------------------------------------------------------------
class Appointment(models.Model):

    doctor = models.ForeignKey(
        "users.Doctor",
        related_name="appointment_doctors",
        on_delete=models.CASCADE,
    )
    patient = models.ForeignKey(
        "users.Patient",
        related_name="appointment_patients",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now=True)
    date = models.DateTimeField()
    description = models.TextField(max_length=500, default="No description")
    status = models.BooleanField(default=False)

    def __str__(self):
        return "({}) ({})".format(self.patient.username, self.doctor.username)


# ---------------------------------------------------------------------------------------------
# ------------------------------------- consultation Models -----------------------------------
# ---------------------------------------------------------------------------------------------
class Consultation(models.Model):
    appointment = models.ForeignKey(
        "appointment.Appointment",
        related_name="appointments",
        on_delete=models.CASCADE,
        default="",
    )
    consultation_date = models.DateTimeField()
    notes = models.TextField(max_length=254)
    diagnosis = models.TextField()
    treatment = models.TextField()

    def __str__(self):
        return str(self.patient_id.username)
