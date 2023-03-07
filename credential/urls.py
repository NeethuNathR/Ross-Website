from django.urls import path,include

from credential import views
appname='credential'

urlpatterns = [
     path('senior/',views.senior,name='senior'),
     path('abouts/', views.abouts, name='abouts'),
     path('services/', views.services, name='services'),
     path('contacts/', views.contacts, name='contacts'),
     path('staff_registration/',views.staff_registration,name='staff_registration'),
     path('change_password/',views.change_password,name='change password'),
     path('staff/',views.staff,name='staff'),
     path('staff_login/',views.staff_login,name='staff_login'),
     path('aboutss/',views.aboutss,name='aboutss'),
     path('servicess/',views.servicess,name='servicess'),
     path('contactss/',views.contactss,name='contactss'),
     path('queries/',views.queries,name='queries'),

]