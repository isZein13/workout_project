from django.urls import path
from .import views 

urlpatterns = [
    path('', views.showprogram, name='show-program')
]