# Generated by Django 3.2.6 on 2021-08-21 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('likes_and_dislikes', '0005_auto_20210821_1227'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ['score', 'nickname']},
        ),
        migrations.RenameField(
            model_name='player',
            old_name='points',
            new_name='score',
        ),
    ]