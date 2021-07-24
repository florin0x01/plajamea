from django.contrib import admin
from django.urls import include, path, re_path
from . import views

urlpatterns = [
#   path('vamaveche', views.index, name='index')
#    re_path(r'[a-zA-Z]+', views.index, name='index')
    path('menu', views.sendMenu, name='menuPDF'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('userhome', views.show_userhome, name='show_userhome'),
    path('<str:numeplaja>', views.numeplaja, name='numeplaja'),
    path('', views.index, name='index')
]
