# Generated by Django 4.0 on 2024-03-14 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programms', '0002_workoutprogram_delete_programms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workoutprogram',
            name='program_picture',
        ),
    ]
