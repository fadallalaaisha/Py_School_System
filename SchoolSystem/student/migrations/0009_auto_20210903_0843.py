# Generated by Django 3.2.5 on 2021-09-03 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_alter_student_passport_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='admintion_number',
            field=models.CharField(default=1, max_length=13),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='student_number',
            field=models.CharField(default=1, max_length=13),
            preserve_default=False,
        ),
    ]
