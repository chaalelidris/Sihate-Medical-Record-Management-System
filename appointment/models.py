from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# ----------------------------------------------------------------------------
# ---------------------------- Appointment model ----------------------------------
# ----------------------------------------------------------------------------
class Appointment(models.Model):

    doctor = models.ForeignKey(
        "users.Doctor",
        related_name="appointment_doctor",
        on_delete=models.CASCADE,
    )
    patient = models.ForeignKey(
        "users.Patient",
        related_name="appointment_patient",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now=True)
    appointment_date = models.DateTimeField()
    description = models.TextField(max_length=500, default="No description")
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.patient_id.username)
