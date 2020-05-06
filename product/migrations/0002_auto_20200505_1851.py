# Generated by Django 3.0.5 on 2020-05-05 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('description', models.CharField(max_length=999)),
                ('release_date', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo', models.CharField(blank=True, max_length=999)),
            ],
        ),
        migrations.CreateModel(
            name='Console',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('description', models.CharField(max_length=999)),
                ('release_date', models.DateField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Brand')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VideoGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('description', models.CharField(max_length=999)),
                ('release_date', models.DateField()),
                ('ageLimit', models.IntegerField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Brand')),
                ('console', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Console')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
        migrations.AddField(
            model_name='accessory',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Brand'),
        ),
    ]
