from django.http import HttpResponse
from django.shortcuts import render
def profile(request):
    return render(request, 'profile.html')

def profile2(request):
    return render(request, 'profile2.html')