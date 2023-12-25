from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.


from django.urls import path
from .models import BlogPost, PostCategory, Comment
from django.http import HttpResponse

from .forms import PostForm


def index(request):
    posts = BlogPost.objects.order_by("-date_posted")
    context = {"posts": posts}
    # return HttpResponse("Hello, world. You're at the Blog main page.")
    return render(request, "blog_app/index.html", context)


@login_required
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
            return redirect("blog_app:index")
    context = {"form": form}
    return render(request, "blog_app/add_post.html", context)


@login_required
def user_posts(request):
    posts = BlogPost.objects.filter(owner=request.user).order_by("-date_posted")
    context = {"posts": posts}
    return render(request, "blog_app/user_posts.html", context)


@login_required
def edit_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    if post.owner != request.user:
        raise Http404
    if request.method != "POST":
        # initial request; pre-fill form with current post
        form = PostForm(instance=post)
    else:
        # POST data submitted; process data
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog_app:user_posts")

    context = {"post": post, "form": form}
    return render(request, "blog_app/edit_post.html", context)
