# Generated by Django 3.0.5 on 2020-05-05 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videogame', '0002_auto_20200505_1851'),
        ('brand', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Brand',
        ),
    ]
