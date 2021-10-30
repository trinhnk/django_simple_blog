from django.contrib import admin

from blog.models import BlogAuthor, BlogCategory, BlogComment, BlogPost

# Register your models here.
@admin.register(BlogAuthor)
class BlogAuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    pass

@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    pass