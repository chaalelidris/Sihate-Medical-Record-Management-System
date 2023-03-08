from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# ----------------------------------------------------------------------------
# ---------------------------- Appointment model ----------------------------------
# ----------------------------------------------------------------------------
class Appointment(models.Model):
    doctorId = models.ForeignKey(
        "doctor.Doctor",
        related_name="appointment_doctor",
        on_delete=models.CASCADE,
    )
    patientId = models.ForeignKey(
        "patient.Patient",
        related_name="appointment_patient",
        on_delete=models.CASCADE,
    )
    appointmentCreationDate = models.DateField(auto_now=True)
    appointmentDate = models.DateTimeField()
    description = models.TextField(max_length=500, default="No description")
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.patientId.username)
