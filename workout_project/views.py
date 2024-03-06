from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, 'home.html')

def reverse(request):
    user_message = request.GET['message']
    reversed_message = user_message[::-1]
    return render(request, 'reverse.html', {'message':user_message, 'rev_message':reversed_message})