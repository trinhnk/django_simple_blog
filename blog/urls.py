from django.urls import path
from . import views

from django.contrib.auth import views as authViews
from blog.forms.loginForm import UserLoginForm

urlpatterns = [
    path('', views.index, name='home'),
    path('post/<int:post_id>/', views.blogPost, name='post'),
    # path('create', views.create, name='create'),
    # path('author/<int:user_id>', views.author, name='author_detail'),
    # path('store', views.store, name='store_post'),
    # path('login', views.login, name='login'),
    # path('register', views.register, name='register')

    path(
        'login/',
        authViews.LoginView.as_view(
            template_name="blog/auth/login.html",
            authentication_form=UserLoginForm
            ),
        name='login'
    ),

    path('register/', views.register_request, name="register"),
]
