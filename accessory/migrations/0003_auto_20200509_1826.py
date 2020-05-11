# Generated by Django 3.0.5 on 2020-05-09 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0004_auto_20200507_1442'),
        ('accessory', '0002_auto_20200507_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('description', models.CharField(max_length=999)),
                ('image', models.CharField(max_length=999)),
                ('release_date', models.DateField()),
                ('age_limit', models.IntegerField(default=3)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brand.Brand')),
                ('console', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accessory.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Accessory',
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accessory.Type'),
        ),
    ]
