from django.contrib import admin
from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [

    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/updateinfo/', views.updateinfo, name='updateinfo')

]
