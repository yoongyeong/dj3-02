# Generated by Django 3.0.9 on 2020-08-07 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('features', models.TextField()),
                ('is_promo', models.BooleanField(default=False)),
                ('is_published', models.BooleanField(default=True)),
                ('image_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('image_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('image_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('image_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('image_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('image_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('image_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.Cluster')),
            ],
        ),
    ]
