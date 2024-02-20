# from django.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name = 'home'),
    path('login/',views.UserSignIn, name='UserSignIN'),
    path('logout/',views.UserLogout, name='UserLogOut'),
    path('register/',views.RegisterUser, name='RegisterUser')
]
