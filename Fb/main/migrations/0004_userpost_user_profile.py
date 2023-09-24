# Generated by Django 4.2.4 on 2023-09-24 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_userprofile_cover_photo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpost',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='main.userprofile'),
        ),
    ]