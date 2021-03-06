# Generated by Django 2.0.1 on 2018-06-16 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20180610_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(default='slug', unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
