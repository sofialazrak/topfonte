# Generated by Django 3.1.6 on 2021-02-22 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
    ]
