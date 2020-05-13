# Generated by Django 3.0.5 on 2020-05-13 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accessory', '0004_auto_20200509_1858'),
        ('user', '0004_auto_20200512_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecentlyViewed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accessory.Product')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='product',
            field=models.ManyToManyField(through='user.RecentlyViewed', to='accessory.Product'),
        ),
    ]
