from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    id_medecin = models.ForeignKey(
        User,
        related_name="rdv_med",
        on_delete=models.CASCADE,
        default="3",
    )
    id_patient = models.ForeignKey(
        User,
        related_name="rdv_patient",
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField()

    num_rdv = models.IntegerField(default="1")

    def __str__(self):
        return str(self.id_patient.username)
