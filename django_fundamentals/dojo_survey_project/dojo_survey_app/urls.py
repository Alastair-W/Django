from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('store_results', views.create_results),
    path('display_results', views.results),
    path('about', views.about_page)
]