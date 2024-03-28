app_name = 'programms'
from django.urls import path
from .import views 

urlpatterns = [
    path('', views.showprogram, name='show-program'),
    path('programms/<int:prog_id>/', views.current_program, name='current-program'),
]