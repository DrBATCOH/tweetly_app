from __future__ import annotations

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.models import CustomUser

from core.models import Follower, CustomUser


def follow_user(user: CustomUser, follower_username: str) -> None:
    user_to_follow = get_object_or_404(CustomUser, username=follower_username)
    if user != user_to_follow:
        Follower.objects.get_or_create(follower=user, following=user_to_follow)


def unfollow_user(user: CustomUser, follower_username: str) -> None:
    user_to_unfollow = get_object_or_404(CustomUser, username=follower_username)
    Follower.objects.filter(follower=user, following=user_to_unfollow).delete()


def get_followers(user: CustomUser):
    user = get_user_model().objects.get(username=user)
    followers = user.follower.all()
    print(followers)
    return followers


def get_followings(user: CustomUser):
    user = get_user_model().objects.get(username=user)
    following = user.following.all()
    print(following)
    return following
