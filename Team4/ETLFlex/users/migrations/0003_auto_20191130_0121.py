# Generated by Django 2.2.7 on 2019-11-30 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191029_1605'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='ftpDirectory',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='ftpPassword',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='ftpURL',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='ftpUsername',
        ),
    ]
