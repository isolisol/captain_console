# Generated by Django 3.0.5 on 2020-05-07 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videogame', '0007_videogame_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videogame',
            name='release_date',
            field=models.DateField(blank=True),
        ),
    ]
