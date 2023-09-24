# Generated by Django 4.2.4 on 2023-09-23 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='cover_photo',
            field=models.ImageField(blank=True, upload_to='cover_photos/'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_photo',
            field=models.ImageField(blank=True, upload_to='profile_photos/'),
        ),
    ]