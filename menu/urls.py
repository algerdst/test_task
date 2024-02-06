from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('menu/<slug:slug>', menu, name='menu'),
]
