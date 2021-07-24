from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('plajamea_web.urls')),
    path('admin/', admin.site.urls),
]