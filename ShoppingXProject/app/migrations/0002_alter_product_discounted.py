# Generated by Django 4.1.2 on 2023-01-25 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discounted',
            field=models.FloatField(),
        ),
    ]
