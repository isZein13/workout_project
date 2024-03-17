from django.db import models

# Create your models here.
class WorkoutProgram(models.Model):
    program_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    program_picture = models.ImageField(upload_to='program_pictures/', blank=True, null=True)

    def __str__(self):
        return self.name
    

class Exercise(models.Model):
    exercise_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    sport_type = models.CharField(max_length=50)
    exercise_picture = models.ImageField(upload_to='exercise_pictures/', blank=True, null=True)
    
    def __str__(self):
        return self.name


class ExerciseWorkoutProgram(models.Model):
    id = models.AutoField(primary_key=True)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    program = models.ForeignKey(WorkoutProgram, on_delete=models.CASCADE)
