# Generated by Django 4.1.5 on 2023-10-04 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0023_product_product_type_alter_product_category_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="product_type",
            field=models.CharField(
                choices=[
                    ("Boxers", "Boxers"),
                    ("Shorts", "Shorts"),
                    ("Extras", "Extras"),
                    ("Strings", "Strings"),
                    ("Ensembles", "Ensembles"),
                    ("Cullotes", "Cullotes"),
                ],
                max_length=20,
                null=True,
            ),
        ),
    ]
