from django.urls import path
from core.presentation.views import (
    index,
    tags,
    profile,
    notifications,
    trending,
    login_controller,
    registration_controller
)


urlpatterns = [
    path("", index, name="home"),
    path("trending/", trending, name="trending"),
    path("profile/", profile, name="profile"),
    path("tags/", tags, name="tags"),
    path("notifications/", notifications, name="notifications"),
    path("login/", login_controller, name="login"),
    path("singup/", registration_controller, name="singup"),
]
