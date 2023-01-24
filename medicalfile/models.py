from django.db import models

# Create your models here.


class FichePatient(models.Model):
    SEX_FEMALE = "F"
    SEX_MALE = "M"
    SEX_UNSURE = "U"

    a = "O+"
    b = "O-"
    c = "A+"
    d = "A-"
    e = "B+"
    f = "B-"
    g = "AB+"
    h = "AB-"

    Celebataire = "celebataire"
    Marié = "Marié"
    Divorcé = "Divorcé"
    veuf = "veuf"

    op = "Oui"
    opp = "Non"
    SEX_OPTIONS = ((SEX_FEMALE, "Female"), (SEX_MALE, "Male"), (SEX_UNSURE, "Unsure"))
    GROUP_SANGUIN_OPTIONS = [
        (a, "O+"),
        (b, "O-"),
        (c, "A+"),
        (d, "A-"),
        (e, "B+"),
        (f, "B-"),
        (g, "AB+"),
        (h, "AB-"),
    ]
    SITUATION_OPTIONS = [
        (Celebataire, "celebataire"),
        (Marié, "Marié"),
        (Divorcé, "Divorcé"),
        (veuf, "veuf"),
    ]
    OPTIONS = [(op, "Oui"), (opp, "Non")]
    id_fiche = models.AutoField(primary_key=True)
    id_patient = models.ForeignKey(
        User,
        related_name="fich_patient",
        on_delete=models.CASCADE,
    )
    id_medecin = models.ForeignKey(
        User,
        related_name="fich_med",
        on_delete=models.CASCADE,
    )
    nom = models.CharField(max_length=254)
    prenom = models.CharField(max_length=254)
    address = models.CharField(max_length=254)
    age = models.IntegerField()
    sexe = models.CharField(max_length=1, choices=SEX_OPTIONS, default=None)
    tel = PhoneNumberField(blank=True)
    email = models.EmailField()
    group_sanguin = models.CharField(
        max_length=3, choices=GROUP_SANGUIN_OPTIONS, default=None
    )
    NSS = models.CharField(max_length=254)
    profession = models.CharField(max_length=254)
    motif_consultation = models.CharField(max_length=254)
    nom_etablissement_universitaire = models.CharField(max_length=254)
    date_naiss = models.DateField()
    lieu_naiss = models.CharField(max_length=254)
    situation = models.CharField(max_length=11, choices=SITUATION_OPTIONS, default=None)
    filiére = models.CharField(max_length=254)
    à_fumer = models.CharField(max_length=3, choices=OPTIONS, default=None)
    à_chiquer = models.CharField(max_length=3, choices=OPTIONS, default=None)
    à_prise = models.CharField(max_length=3, choices=OPTIONS, default=None)
    nbr_cigarettes = models.IntegerField(blank=True)
    nbr_boites = models.IntegerField(blank=True)
    age_à_la_premiére_prise = models.IntegerField()
    ancien_fumeur = models.CharField(max_length=3, choices=OPTIONS, default=None)
    periode_exposition = models.IntegerField(blank=True)
    Affections_congénitales = models.TextField(max_length=254)
    Maladies_génerale = models.TextField(max_length=254)
    Interventions_chirurgicales = models.TextField(max_length=254)
    Réactions_allergique_aux_médicaments = models.TextField(max_length=254)

    def __str__(self):
        return str(self.id_patient.username)
