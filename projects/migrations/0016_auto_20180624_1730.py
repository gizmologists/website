# Generated by Django 2.0.1 on 2018-06-24 17:30

from django.db import migrations


class Migration(migrations.Migration):
    atomic=False

    dependencies = [
        ('projects', '0015_auto_20180624_1728'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Temp',
            new_name='User',
        ),
    ]
