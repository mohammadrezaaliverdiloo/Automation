from django.urls import path,include


urlpatterns = [
    
    path('mikrotik/',include('Mikrotik.urls')),
    path('cisco/',include('Cisco.urls')),
    path('ws/',include('WS.urls')),
    path('lx',include('LX.urls')),

]
