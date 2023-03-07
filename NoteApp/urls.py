from django.contrib import admin
from django.urls import path,include

from NoteApp import views
appname='Noteapp'
urlpatterns = [

    path('',views.demo,name='demo'),
    path('about/',views.about,name='about'),
    path('service/',views.service,name='service'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.login,name='login'),
    path('careers/',views.careers,name='careers'),
    path('register/',views.register,name='register'),
    path('senior/',views.senior,name='senior'),
    path('logout/',views.logout,name='logout'),
]
