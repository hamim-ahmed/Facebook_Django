# Generated by Django 3.2.6 on 2023-04-11 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='AppUsers',
        ),
    ]
