# Generated by Django 3.1.2 on 2020-12-14 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0002_choicemodel_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choicemodel',
            name='user',
        ),
    ]