from django.urls import path
from . import views

urlpatterns = [
    path('', views.word_gen),
    path('word_gen_page', views.run_word_gen),
    path('reset', views.reset)
]