from django.contrib import admin

# Register your models here.
from .models import BlogPost, PostCategory, Comment

admin.site.register(BlogPost)
admin.site.register(PostCategory)
admin.site.register(Comment)
