<<<<<<< HEAD
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
=======
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Post
from .forms import NewCommentForm

def home(request):

    all_posts = Post.newmanager.all()

    return render(request, 'post_list.html', {'posts' : all_posts})

def post_single(request, post):

    post = get_object_or_404(Post, slug=post, status='published')

    comments = post.comments.filter(status=True)

    user_comment = None

    if request.method == 'POST':
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.post = post
            user_comment.save()
        return HttpResponseRedirect("/" + post.slug)
    else:
        comment_form = NewCommentForm()
    return render(request, 'post_detail.html', {'post': post, 'comments': user_comment, 'comments': comments, 'comment_form': comment_form})
>>>>>>> Form
