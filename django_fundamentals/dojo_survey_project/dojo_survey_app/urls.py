from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index),
    path('results', views.results),
    path('about', views.about_page)

]