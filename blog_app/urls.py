from django.urls import path

from . import views

app_name = "blog_app"

urlpatterns = [
    # home page
    path("", views.index, name="index"),
    # add new post
    path("add_post/", views.add_post, name="add_post"),
    # page that shows all user's posts
    path("user_posts/", views.user_posts, name="user_posts"),
    # edit post
    path("edit_post/<int:post_id>/", views.edit_post, name="edit_post"),
]
