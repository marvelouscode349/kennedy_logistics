# Generated by Django 4.1.7 on 2023-09-13 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_alter_payment_payment_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_plan',
            field=models.CharField(choices=[('One-month', 'One-month'), ('Six-month', 'Two-month'), ('Twelve-month', 'Twelve-month')], max_length=50, null=True),
        ),
    ]
