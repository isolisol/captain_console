# Generated by Django 3.0.5 on 2020-05-12 11:52

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200509_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='country',
            field=django_countries.fields.CountryField(default=1, max_length=2),
            preserve_default=False,
        ),
    ]