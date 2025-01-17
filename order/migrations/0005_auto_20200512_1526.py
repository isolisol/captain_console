# Generated by Django 3.0.5 on 2020-05-12 15:26

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20200512_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinformation',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contactinformation',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contactinformation',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='contactinformation',
            name='first_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contactinformation',
            name='house_number',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contactinformation',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contactinformation',
            name='postal_code',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
