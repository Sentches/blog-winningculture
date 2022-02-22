from django.urls import path
from . import views
from django import template

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('<slug:post>/', views.post_single, name='post_single'),
]