from django.db import models
from django.contrib.auth.models import User

# Doctor models .


class Consultation(models.Model):
    id_consultation = models.AutoField(primary_key=True)

    id_patient = models.ForeignKey(
        User,
        related_name="cons_patient",
        on_delete=models.CASCADE,
    )
    contenue = models.TextField(max_length=254)
    antecedant = models.CharField(max_length=254)
    traitement = models.CharField(max_length=254)
    date_consultation = models.DateTimeField()

    def __str__(self):
        return str(self.id_patient.username)
