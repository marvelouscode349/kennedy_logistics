# Generated by Django 4.1.7 on 2023-07-24 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_profile_id_verification_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id_verification',
            field=models.ImageField(upload_to='photos/id'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='passport',
            field=models.ImageField(default='default.jpg', upload_to='photos/passports'),
        ),
    ]