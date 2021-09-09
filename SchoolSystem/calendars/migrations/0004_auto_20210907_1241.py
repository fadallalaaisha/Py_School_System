# Generated by Django 3.2.5 on 2021-09-07 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0003_auto_20210903_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Calendar',
        ),
    ]
