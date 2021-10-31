from django.shortcuts import render

from .models import BlogPost
from random import randrange

# Create your views here.
def index(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/page/home.html', {'posts': posts})

def blogPost(request, post_id):
    if not post_id:
        latestId = BlogPost.objects.latest('id').id
        post = BlogPost.objects.get(id=randrange(1,4))
    else:
        post = BlogPost.objects.get(id=post_id)
    return render(request, 'blog/page/post.html', {'post': post})