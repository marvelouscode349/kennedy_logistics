# Generated by Django 4.1.7 on 2023-08-20 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_remove_order_is_completed_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_complete',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order'),
        ),
    ]