# Generated by Django 5.0 on 2023-12-07 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20231205_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_interest',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]