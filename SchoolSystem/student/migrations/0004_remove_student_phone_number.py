# Generated by Django 3.2.5 on 2021-07-31 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20210731_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='phone_number',
        ),
    ]
