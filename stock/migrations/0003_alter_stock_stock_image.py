# Generated by Django 4.1.7 on 2023-08-07 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_stock_stock_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='stock_image',
            field=models.ImageField(upload_to='stocks_images'),
        ),
    ]
