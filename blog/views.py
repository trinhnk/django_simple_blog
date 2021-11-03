from django.shortcuts import render

from blog.forms.registerForm import UserRegisterForm

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

def register_request(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = UserRegisterForm()
	return render (request=request, template_name="blog/auth/register.html", context={"register_form":form})