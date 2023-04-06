# Generated by Django 4.1.5 on 2023-03-14 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Appointment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("appointment_date", models.DateTimeField()),
                (
                    "description",
                    models.TextField(default="No description", max_length=500),
                ),
                ("status", models.BooleanField(default=False)),
                (
                    "doctor_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="appointment_doctor",
                        to="users.doctor",
                    ),
                ),
                (
                    "patient_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="appointment_patient",
                        to="users.patient",
                    ),
                ),
            ],
        ),
    ]
