# Generated by Django 3.0.5 on 2020-05-07 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brand', '0003_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Console',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('description', models.CharField(max_length=999)),
                ('release_date', models.DateField()),
                ('image', models.CharField(max_length=999)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='brand.Brand')),
            ],
        ),
    ]
