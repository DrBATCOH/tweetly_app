from __future__ import annotations

from core.models import CustomUser, Follower
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from .notification import create_notification


def follow_user(user: CustomUser, follower_username: str) -> None:
    user_to_follow = get_object_or_404(CustomUser, username=follower_username)
    if user != user_to_follow:
        Follower.objects.get_or_create(follower=user, following=user_to_follow)
        message = f"{user.first_name} {user.last_name} follow to you"
        create_notification(recipient=user_to_follow, message=message)


def unfollow_user(user: CustomUser, follower_username: str) -> None:
    user_to_unfollow = get_object_or_404(CustomUser, username=follower_username)
    Follower.objects.filter(follower=user, following=user_to_unfollow).delete()
    message = f"{user.first_name} {user.last_name} unfollowed you"
    create_notification(recipient=user_to_unfollow, message=message)


def get_followers(user: CustomUser):
    user = get_user_model().objects.get(username=user)
    followers = user.follower.all()
    return followers


def get_followings(user: CustomUser):
    user = get_user_model().objects.get(username=user)
    following = user.following.all()
    return following


def get_possible_follower(user: CustomUser, country: str) -> list[Follower]:
    users_in_country = CustomUser.objects.filter(country=country).exclude(id=user.id)
    possible_followers = users_in_country.exclude(follower__follower=user)
    possible_followers = possible_followers[:10]
    return possible_followers
