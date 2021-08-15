# Generated by Django 3.2.5 on 2021-07-31 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=12)),
                ('course_code', models.IntegerField()),
                ('syllabus', models.FileField(upload_to='')),
                ('course_duration', models.DateField()),
                ('trainer_course', models.CharField(max_length=10)),
                ('projects', models.TextField()),
            ],
        ),
    ]
