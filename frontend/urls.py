from django.urls import path, include
from django.conf import settings
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('recordings/', recordings, name='recordings'),
    path('events/', events, name='events'),
    path('logout/', logout, name='logout'),
    path('view_video/output/<str:video>/', view_video, name='view_video'),
]
