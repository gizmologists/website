# Generated by Django 2.0.1 on 2018-06-17 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='woof', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]