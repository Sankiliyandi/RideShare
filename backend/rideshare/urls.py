from django.contrib import admin
from django.urls import path, include
from .views import *


 
urlpatterns = [
    path('', home,name='Home'),
    path('register', register,name='register'), 
    # path('registerform/' ,formHandle,name='signup'),
    path('otp' ,otpScreen,name='otp'),
    path('login' ,loginform,name='loginform'),
    path('logout' ,logout,name='logout'),
    path('search',searchRide,name='search'),
    path('offer',offerpost,name='offer'),
]