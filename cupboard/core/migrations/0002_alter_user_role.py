# Generated by Django 5.0.7 on 2024-07-22 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[
                    ("admin", "Admin"),
                    ("shopkeeper", "Shopkeeper"),
                    ("staff", "Staff"),
                    ("manager", "Manager"),
                ],
                max_length=10,
            ),
        ),
    ]
