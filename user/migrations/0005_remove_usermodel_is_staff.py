# Generated by Django 5.0 on 2024-01-03 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_usermodel_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='is_staff',
        ),
    ]
