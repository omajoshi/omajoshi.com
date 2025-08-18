from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post

# Create your views here.

class PostList(ListView):
    model = Post
    paginate_by = 10

class PostListTitleOnly(ListView):
    model = Post
    template_name = 'blog/post_list_title_only.html'

class PostDetail(DetailView):
    model = Post
