from django.urls import path,include
from . import views

urlpatterns = [
    path('home/', views.home, name= "home"),
    path('devices/', views.devices, name= "devices"),
    path('configure/', views.configure, name= "config"),
    path('verify_config/', views.verify_config, name= "verify_config"),
    path('logs/', views.logs, name= "logs"),
]
