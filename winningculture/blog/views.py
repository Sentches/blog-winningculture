from xml.etree.ElementTree import Comment
from django.views.generic import DetailView, ListView, CreateView
from .models import Post, Comment

class PostListView(ListView):
    model = Post 

class PostDetailView(DetailView):
    model = Post

class CommentView(CreateView):
    model = Comment
    template_name = 'add_comment.html'
    fields = '__all__'