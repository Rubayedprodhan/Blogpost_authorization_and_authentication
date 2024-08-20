from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
   
    path('register/', views.register,name='register'),
    path('loging/', views.user_login,name='loging'),
    path('logout/', views.user_logout,name='user_logout'),
   
    path('profile/', views.profile,name='profile'),
    path('profile/edit', views.profile_edit,name='edit_profile'),
    path('profile/edit/passwordchange', views.profile_edit_password_change,name='profile_edit_password_change'),
    
]