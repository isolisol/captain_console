# Generated by Django 3.0.5 on 2020-05-07 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videogame', '0005_auto_20200507_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoGameHasGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='videogame.Genre')),
                ('video_game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='videogame.VideoGame')),
            ],
        ),
    ]
