# Generated by Django 2.0.1 on 2018-06-17 17:04

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='Body goes here'),
            preserve_default=False,
        ),
    ]
