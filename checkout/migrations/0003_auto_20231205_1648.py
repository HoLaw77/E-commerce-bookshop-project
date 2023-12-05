# Generated by Django 3.2.23 on 2023-12-05 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_orderdetail_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='item_total',
            field=models.DecimalField(decimal_places=2, default='0.0', editable=False, max_digits=6),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
