# Generated by Django 3.2.6 on 2021-08-21 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('likes_and_dislikes', '0002_auto_20210820_2152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='likes',
            new_name='like',
        ),
    ]
