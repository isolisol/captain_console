# Generated by Django 3.0.5 on 2020-05-14 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_recentlyviewed_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recentlyviewed',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
