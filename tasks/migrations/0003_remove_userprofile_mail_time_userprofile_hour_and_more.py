# Generated by Django 4.0.1 on 2022-02-21 20:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_userprofile_mail_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='mail_time',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='hour',
            field=models.IntegerField(default=19, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(23)]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='minute',
            field=models.IntegerField(default=30, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(59)]),
        ),
    ]