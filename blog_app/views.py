from django.shortcuts import render, redirect

# Create your views here.


from django.urls import path
from .models import BlogPost, PostCategory, Comment
from django.http import HttpResponse


def index(request):
    posts = BlogPost.objects.order_by("-date_posted")
    context = {"posts": posts}
    # return HttpResponse("Hello, world. You're at the Blog main page.")
    return render(request, "blog_app/index.html", context)


def add_post(request):
    if request.method != "POST":
        # no data submitted; create blank form
        form = PostForm()
    else:
        # POST data submitted; process data
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            form.save()
            return redirect("blog_app:index")
    context = {"form": form}
    return render(request, "blog_app/add_post.html", context)
