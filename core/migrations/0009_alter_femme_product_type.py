# Generated by Django 4.1.5 on 2023-09-19 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_alter_homme_product_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="femme",
            name="product_type",
            field=models.CharField(
                choices=[
                    ("Strings", "Strings"),
                    ("Ensembles", "Ensembles"),
                    ("Cullotes", "Cullotes"),
                ],
                default="Strings",
                max_length=50,
            ),
        ),
    ]
