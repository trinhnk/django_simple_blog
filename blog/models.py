from django.db import models
from django.conf import settings

# Create your models here.
class BlogAuthor(models.Model):
    nickname = models.CharField(max_length=45)
    facebook = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
        verbose_name="user id", on_delete=models.SET_NULL)
    def __str__(self):
        return self.nickname

class BlogCategory(models.Model):
    name = models.CharField(max_length=45)
    slug = models.SlugField(max_length=45)
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.name

class BlogPost(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.CharField(max_length=500)
    content = models.TextField(max_length=2000, null=True)
    published_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(BlogAuthor, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name

class BlogComment(models.Model):
    content = models.CharField(max_length=500)
    status = models.BooleanField(default=True)
    post = models.ForeignKey(BlogPost, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
        verbose_name="user id", on_delete=models.SET_NULL)
