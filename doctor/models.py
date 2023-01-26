from django.db import models
from django.contrib.auth.models import User

# Doctor models .


class Consultation(models.Model):
    id_consultation = models.AutoField(primary_key=True)
    id_medecin = models.ForeignKey(
        User,
        related_name="cons_medecin",
        on_delete=models.CASCADE,
    )
    id_patient = models.ForeignKey(
        User,
        related_name="cons_patient",
        on_delete=models.CASCADE,
    )
    id_facture = models.ForeignKey(
        "Facture",
        related_name="cons_fact",
        on_delete=models.CASCADE,
    )
    contenue = models.TextField(max_length=254)
    antecedant = models.CharField(max_length=254)
    traitement = models.CharField(max_length=254)
    date_consultation = models.DateTimeField()

    def __str__(self):
        return str(self.id_patient.username)


class Facture(models.Model):
    id_facture = models.AutoField(primary_key=True)
    # id_consultation = models.ForeignKey('Consultation',related_name="facture_consultation",on_delete=models.CASCADE, )
    prix = models.FloatField()
    date = models.DateTimeField()

    def __str__(self):
        return str(self.date)
