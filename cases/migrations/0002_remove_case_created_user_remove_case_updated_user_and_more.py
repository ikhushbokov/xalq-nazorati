# Generated by Django 5.1.6 on 2025-02-11 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='created_user',
        ),
        migrations.RemoveField(
            model_name='case',
            name='updated_user',
        ),
        migrations.RemoveField(
            model_name='case',
            name='user',
        ),
    ]
