# Generated by Django 4.1.7 on 2023-08-14 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_order_order_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='rider',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
