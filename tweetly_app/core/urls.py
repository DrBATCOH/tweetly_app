from django.urls import path
from core.views import (
    index,
    tags,
    profile,
    notifications,
    trending
)



urlpatterns = [
    path("", index, name="home"),
    path("trending/", trending, name="trending"),
    path("profile/", profile, name="profile"),
    path("tags/", tags, name="tags"),
    path("notifications/", notifications, name="notifications"),
]
