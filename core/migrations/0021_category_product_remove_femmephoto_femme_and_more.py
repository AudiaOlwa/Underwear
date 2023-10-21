# Generated by Django 4.1.5 on 2023-10-04 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0020_remove_cart_product_cart_homme_delete_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("nom", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("nom", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="products/")),
                ("description", models.TextField()),
                ("prix", models.DecimalField(decimal_places=0, max_digits=5)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.category"
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="femmephoto",
            name="femme",
        ),
        migrations.RemoveField(
            model_name="hommephoto",
            name="homme",
        ),
        migrations.DeleteModel(
            name="Cart",
        ),
        migrations.DeleteModel(
            name="Femme",
        ),
        migrations.DeleteModel(
            name="FemmePhoto",
        ),
        migrations.DeleteModel(
            name="Homme",
        ),
        migrations.DeleteModel(
            name="HommePhoto",
        ),
    ]