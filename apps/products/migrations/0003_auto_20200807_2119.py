# Generated by Django 3.0.9 on 2020-08-07 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200807_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='area_length',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='area_width',
            field=models.IntegerField(default=None),
        ),
    ]
