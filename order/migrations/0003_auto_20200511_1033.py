# Generated by Django 3.0.5 on 2020-05-11 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20200511_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productincart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
