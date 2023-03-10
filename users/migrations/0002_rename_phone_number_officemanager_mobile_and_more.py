# Generated by Django 4.1.5 on 2023-03-10 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="officemanager",
            old_name="phone_number",
            new_name="mobile",
        ),
        migrations.AddField(
            model_name="officemanager",
            name="profile_pic",
            field=models.ImageField(
                blank=True, null=True, upload_to="profile_pic/OfficeManagerProfilePic/"
            ),
        ),
    ]
