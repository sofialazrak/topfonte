# Generated by Django 3.1.6 on 2021-03-10 15:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20210302_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message='Entrez un numéro de téléphone valide', regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]