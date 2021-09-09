# Generated by Django 3.2.5 on 2021-08-27 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=10, null=True)),
                ('event_month', models.CharField(max_length=10, null=True)),
                ('event_date', models.DateTimeField(blank=2, null=True)),
                ('event_organizer', models.CharField(max_length=10, null=True)),
                ('event_duration', models.TimeField(null=True)),
                ('event_goals', models.CharField(max_length=14, null=True)),
                ('event_appoved', models.CharField(max_length=12, null=True)),
                ('event_attented_by', models.CharField(max_length=3, null=True)),
            ],
        ),
    ]
