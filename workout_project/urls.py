from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .import views
import programms.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('programs/', programms.views.home, name='programs'),
    path('program/', include('programms.urls'), name='program'),
    path('reversed/', views.reverse, name='reverse'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
