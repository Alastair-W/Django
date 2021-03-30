from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registerPage', views.registerPage, name='registerPage'),
    path('signUp', views.signUp, name='signUp'),
    path('authenticate', views.authenticate, name='authenticate'),
    path('logIn', views.logIn, name='logIn'),
    path('logOut', views.logOut, name='logOut'),
    path('creditCards', views.creditCards, name='creditCards'),
    path('displayCC/<int:ccID>', views.displayCC, name='displayCC'),
    path('favorite/<int:ccID>', views.favorite, name='favorite'),
    path('retailers', views.retailers, name='retailers'),
    path('favoriteRetail/<int:retailID>', views.favoriteRetail, name='favoriteRetail'),
    path('seeFavorites', views.seeFavorites, name='seeFavorites'),
    path('emailCheck', views.emailCheck, name='emailCheck')
]