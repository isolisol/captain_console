# Generated by Django 3.0.5 on 2020-05-09 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accessory', '0003_auto_20200509_1826'),
        ('videogame', '0012_auto_20200507_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videogamehasgenre',
            name='video_game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accessory.Product'),
        ),
        migrations.DeleteModel(
            name='VideoGame',
        ),
    ]
