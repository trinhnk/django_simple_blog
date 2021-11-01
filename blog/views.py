from django.shortcuts import render

from .models import BlogPost
from random import randrange

# Create your views here.
def index(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/page/home.html', {'posts': posts})

def login(request):
    return render(request, 'blog/auth/login.html')

def register(request):
    return render(request, 'blog/auth/register.html')

def blogPost(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    return render(request, 'blog/page/post.html', {'post': post})