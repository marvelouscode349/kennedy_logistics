# Generated by Django 4.1.7 on 2023-08-09 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
