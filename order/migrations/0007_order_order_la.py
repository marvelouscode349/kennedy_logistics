# Generated by Django 4.1.7 on 2023-08-14 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_order_order_size_order_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_la',
            field=models.CharField(choices=[('agege', 'Agege'), ('ajeromi-ifelodun', 'Ajeromi-Ifelodun'), ('alimosho', 'Alimosho'), ('amuwo-odofin', 'Amuwo-Odofin'), ('apapa', 'Apapa'), ('badagry', 'Badagry'), ('epe', 'Epe'), ('etesatolocalgovernment', 'Eti-Osa'), ('ibeju-lekki', 'Ibeju-Lekki'), ('ifako-ijaiye', 'Ifako-Ijaiye'), ('ikeja', 'Ikeja'), ('ikorodu', 'Ikorodu'), ('kosofe', 'Kosofe'), ('lagos-island', 'Lagos Island'), ('lagos-mainland', 'Lagos Mainland'), ('mushin', 'Mushin'), ('ojo', 'Ojo'), ('oshodi-isolo', 'Oshodi-Isolo'), ('somolu', 'Somolu'), ('surulere', 'Surulere')], max_length=50, null=True),
        ),
    ]
