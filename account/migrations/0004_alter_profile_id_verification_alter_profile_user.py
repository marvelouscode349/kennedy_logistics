# Generated by Django 4.1.7 on 2023-07-24 04:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id_verification',
            field=models.ImageField(default='default.jpg', upload_to='photos/id'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]