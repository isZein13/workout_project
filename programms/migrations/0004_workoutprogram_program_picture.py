# Generated by Django 4.0 on 2024-03-14 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programms', '0003_remove_workoutprogram_program_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='workoutprogram',
            name='program_picture',
            field=models.ImageField(blank=True, null=True, upload_to='exercise_pictures/'),
        ),
    ]
