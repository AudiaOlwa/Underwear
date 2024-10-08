# Generated by Django 4.1.4 on 2023-07-06 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_hommephoto"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hommephoto",
            name="image",
            field=models.ImageField(upload_to="images/"),
        ),
        migrations.CreateModel(
            name="FemmePhoto",
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
                ("image", models.ImageField(upload_to="images/")),
                (
                    "femme",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photos",
                        to="core.femme",
                    ),
                ),
            ],
        ),
    ]
