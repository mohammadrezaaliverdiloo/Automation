from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('harry/',include('HarryPotter.urls')),
    path('', include('automation.urls')),
]
