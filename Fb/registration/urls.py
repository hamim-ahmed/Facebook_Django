from django.contrib import admin
from django.urls import path
from . import views
from django.urls import include

# app_name = 'registration'

urlpatterns = [

    path('testfunction/', views.testfunction, name='testfunction'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('', include('main.urls')),

]