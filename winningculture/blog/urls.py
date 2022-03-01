from unicodedata import name
from django.urls import path
from . import views
from django import template

app_name = 'blog'

urlpatterns = [
<<<<<<< HEAD
    path("", views.PostListView.as_view(), name="list"),
    path("<slug:slug>/", views.PostDetailView.as_view(), name="detail"),
    path("<slug:title>/add-comment", views.CommentView.as_view(), name="commentview")
=======
    path('', views.home, name='homepage'),
    path('<slug:post>/', views.post_single, name='post_single'),
>>>>>>> Form
]