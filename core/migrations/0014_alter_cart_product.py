# Generated by Django 4.1.5 on 2023-10-03 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0013_remove_cart_homme_cart_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="core.product"
            ),
        ),
    ]
