# Generated by Django 4.1.5 on 2023-04-13 14:17

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
                ("date", models.DateTimeField()),
                (
                    "description",
                    models.TextField(default="No description", max_length=500),
                ),
                ("status", models.BooleanField(default=False)),
                (
                    "doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="appointment_doctors",
                        to="users.doctor",
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="appointment_patients",
                        to="users.patient",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Consultation",
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
                ("consultation_date", models.DateTimeField()),
                ("notes", models.TextField(max_length=254)),
                ("diagnosis", models.TextField()),
                ("treatment", models.TextField()),
                (
                    "appointment",
                    models.ForeignKey(
                        default="",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="appointments",
                        to="appointment.appointment",
                    ),
                ),
            ],
        ),
    ]