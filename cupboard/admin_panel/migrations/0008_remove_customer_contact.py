# Generated by Django 5.0.7 on 2024-07-28 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("admin_panel", "0007_rename_customer_invoice_customer_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="contact",
        ),
    ]
