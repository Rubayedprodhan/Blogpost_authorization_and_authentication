from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.post_new, name='post_new'),
    path('edit/<int:id>/', views.edit_post, name='edit_post'),
    path('delete/<int:id>/', views.delete_post, name='delete_post'),
   
]

