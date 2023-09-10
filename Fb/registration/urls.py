from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('testfunction/', views.testfunction, name='testfunction'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),

]