from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register),
    path('secure', views.secure),
    path('logout', views.logout),
    path('loginPage', views.loginPage),
    path('userLogin', views.userLogin),
    path('navigate', views.navigate),
    path('retailers', views.retailers),
    path('creditCards', views.creditCards),
    path('favorite/<int:cc_ID>', views.favorite),
    path('favProfile/<int:cc_ID>', views.favProfile)
]