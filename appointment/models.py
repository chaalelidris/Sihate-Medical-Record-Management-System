from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Appointment(models.Model):
    id_appointment = models.AutoField(primary_key=True)
    id_doctor = models.ForeignKey(
        User, related_name="appointment_doctor", on_delete=models.CASCADE, default="3"
    )
    id_patient = models.ForeignKey(
        User, related_name="appointment_patient", on_delete=models.CASCADE
    )
    date_appointment = models.DateTimeField()
    reason_appointment = models.CharField(max_length=255)
    location_appointment = models.CharField(max_length=255)
    notes_appointment = models.TextField(blank=True)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id_patient.username)
