# Generated by Django 3.0.5 on 2020-05-07 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videogame', '0011_remove_videogame_age_limit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videogame',
            name='release_date',
        ),
        migrations.AddField(
            model_name='videogame',
            name='age_limit',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
