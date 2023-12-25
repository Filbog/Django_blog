from django.urls import path, include

from . import views

app_name = "accounts"
urlpatterns = [
    # Include deafault auth urls
    path("", include("django.contrib.auth.urls")),
    # registration page
    path("register/", views.register, name="register"),
]
