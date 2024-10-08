# Generated by Django 4.1.5 on 2023-09-19 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_alter_femme_product_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="homme",
            name="product_type",
            field=models.CharField(
                choices=[("Boxers", "Boxers"), ("Shorts", "Shorts")],
                default="Boxers",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="femme",
            name="product_type",
            field=models.CharField(
                choices=[
                    ("Strings", "Strings"),
                    ("Soutien-gorges", "Soutien-gorges"),
                    ("Cullotes", "Cullotes"),
                ],
                default="Strings",
                max_length=50,
            ),
        ),
    ]
