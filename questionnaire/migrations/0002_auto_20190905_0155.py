# Generated by Django 2.2.5 on 2019-09-04 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Choices',
            new_name='Choice',
        ),
    ]