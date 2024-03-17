from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views
import programms.views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import YourModelViewSet


router = DefaultRouter()
router.register(r'your-models', YourModelViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('programs/', programms.views.home, name='programs'),
    path('reversed/', views.reverse, name='reverse'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
