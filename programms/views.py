from django.shortcuts import render
from .models import WorkoutProgram, Exercise, ExerciseWorkoutProgram
# Create your views here.
def home(request):
    programs = WorkoutProgram.objects
    return render(request, 'programms.html', {'programs' : programs})

def showprogram(request):
    exercise = Exercise.objects
    return render(request, 'split.html', {'exercise' : exercise})