from django.shortcuts import render, get_list_or_404
from .models import WorkoutProgram, Exercise, ExerciseWorkoutProgram
# Create your views here.
def home(request):
    programs = WorkoutProgram.objects
    return render(request, 'programms.html', {'programs' : programs})

def showprogram(request):
    exercise = Exercise.objects
    return render(request, 'split.html', {'exercise' : exercise})

def current_program(request, prog_id):
    current_prog = get_list_or_404(WorkoutProgram, pk = prog_id)
    return render(request, 'progdescription.html', {'current':current_prog})