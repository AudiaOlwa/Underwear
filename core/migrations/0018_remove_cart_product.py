# Generated by Django 4.1.5 on 2023-10-03 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0017_cart_product"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="product",
        ),
    ]