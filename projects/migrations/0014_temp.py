# Generated by Django 2.0.1 on 2018-06-24 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_auto_20180623_0109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('comp_id', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('graduation_year', models.IntegerField(blank=True, null=True)),
                ('degree_program', models.CharField(blank=True, choices=[('BS', "Bachelor's"), ('MS', "Master's"), ('PHD', 'Doctorate'), ('O', 'Other')], default='BS', max_length=3, null=True)),
                ('major', models.CharField(blank=True, default='Undecided', max_length=50, null=True)),
                ('need_added_to_email', models.BooleanField(default=False)),
                ('need_removed_from_email', models.BooleanField(default=False)),
            ],
        ),
    ]