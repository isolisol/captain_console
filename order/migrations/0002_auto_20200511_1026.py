# Generated by Django 3.0.5 on 2020-05-11 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accessory', '0004_auto_20200509_1858'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Quantity',
            new_name='ProductInCart',
        ),
    ]
