from django.contrib import admin
from .models import WorkoutProgram, Exercise, ExerciseWorkoutProgram
# Register your models here.
admin.site.register(WorkoutProgram)
admin.site.register(Exercise)
admin.site.register(ExerciseWorkoutProgram)