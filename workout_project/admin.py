from django.contrib import admin
from .models import Exercise, WorkoutProgram, ExerciseWorkoutProgram, User


admin.site.register(Exercise)
admin.site.register(WorkoutProgram)
admin.site.register(ExerciseWorkoutProgram)
admin.site.register(User)