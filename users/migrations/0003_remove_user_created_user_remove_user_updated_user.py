# Generated by Django 5.1.6 on 2025-02-11 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created_user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='updated_user',
        ),
    ]
