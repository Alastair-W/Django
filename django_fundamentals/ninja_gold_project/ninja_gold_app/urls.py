from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('earn', views.farm_gold),
    path('refresh', views.refresh)
]