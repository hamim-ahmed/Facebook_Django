from django.contrib import admin
from django.urls import path
from . import views



app_name = 'main'
urlpatterns = [

    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('requested_profile/', views.requested_profile, name='requested_profile'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/updateinfo/', views.updateinfo, name='updateinfo'),
    path('profile/updatepost/', views.updatePost, name ='updatepost'),
    path('createPost/', views.createPost, name='createPost'),  #create post from home
    path('profile/createPost/', views.createPost, name='createPost'),  #create post from profile
    path('updatepost/', views.updatePost, name='updatepost'),
    path('deletepost//<str:id>/', views.deletePost, name='deletepost')

]
