from __future__ import annotations

from typing import TYPE_CHECKING
from core.business_logic.services import follow_user, unfollow_user, get_followings, get_followers
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

if TYPE_CHECKING:
    from django.http import HttpRequest


@require_http_methods(request_method_list=["POST"])
def follow(request: HttpRequest, username: str) -> HttpResponse:
    user = request.user
    follow_user(user, follower_username=username)
    return redirect(to=request.META.get("HTTP_REFERER"))


@require_http_methods(request_method_list=["POST"])
def unfollow(request: HttpRequest, username: str) -> HttpResponse:
    user = request.user
    unfollow_user(user, follower_username=username)
    return redirect(to=request.META.get("HTTP_REFERER"))


def all_follower(request: HttpRequest) -> HttpResponse:
    user = request.user
    print(user.username)
    followers = get_followers(user=user.username)
    context = {"followers": followers}
    return render(request=request, template_name="all_follower.html", context=context)


def all_following(request: HttpRequest) -> HttpResponse:
    user = request.user
    
    followings = get_followings(user=user.username)
    context = {"followings": followings}
    return render(request=request, template_name="all_following.html", context=context )