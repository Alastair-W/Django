from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dojoForm', views.dojoForm),
    path('ninjaForm', views.ninjaForm)
]