# Generated by Django 5.0 on 2023-12-10 12:03

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0013_alter_order_countries'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='countries',
            field=django_countries.fields.CountryField(default='USA', max_length=2),
        ),
    ]