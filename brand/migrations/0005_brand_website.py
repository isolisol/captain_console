# Generated by Django 3.0.5 on 2020-05-11 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0004_auto_20200507_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='website',
            field=models.CharField(default='www.', max_length=999),
            preserve_default=False,
        ),
    ]
