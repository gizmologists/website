# Generated by Django 2.0.1 on 2018-06-09 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20180609_1655'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='person_id',
            new_name='id',
        ),
    ]
