from django.shortcuts import render
from .models import WorkoutProgram
# Create your views here.
def home(request):
    programs = WorkoutProgram.objects
    return render(request, 'programms.html', {'programs' : programs})