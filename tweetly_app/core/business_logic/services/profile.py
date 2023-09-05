from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from django.http import HttpRequest

from core.models import Follower, Tweet
from core.presentation.paginator import CustomPagination, PageNotExists
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.utils import timezone


def get_user_profile(user_profile: get_user_model, page_number: int) -> dict[Any, Any]:
    last_login = user_profile.last_login
    is_online = (timezone.now() - last_login).seconds > 120
    tweets = Tweet.objects.filter(
        Q(author=user_profile) | Q(retweet__user=user_profile)
    ).order_by("-created_at")
    paginator = CustomPagination(per_page=4)

    try:
        tweets_paginated = paginator.paginate(data=tweets, page_number=page_number)
    except PageNotExists:
        raise HttpResponseBadRequest("Page doesn't exist.")

    return {
        "is_online": is_online,
        "paginated": tweets_paginated.data,
        "next_page": tweets_paginated.next_page,
        "prev_page": tweets_paginated.prev_page,
    }


def get_author_profile(request: HttpRequest, username: str) -> dict[Any, Any]:
    author = get_object_or_404(get_user_model(), username=username)
    last_login = author.last_login
    is_online = (timezone.now() - last_login).seconds > 300
    tweets = Tweet.objects.filter(Q(author=author) | Q(retweet__user=author)).order_by(
        "-created_at"
    )
    page_number = request.GET.get("page", 1)
    paginator = CustomPagination(per_page=4)
    is_following = False

    if request.user.is_authenticated:
        is_following = Follower.objects.filter(
            follower=author, following=request.user
        ).exists()

    try:
        tweets_paginated = paginator.paginate(data=tweets, page_number=page_number)
    except PageNotExists:
        raise HttpResponseBadRequest("Page doesn't exist.")

    return {
        "author": author,
        "is_online": is_online,
        "paginated": tweets_paginated.data,
        "next_page": tweets_paginated.next_page,
        "prev_page": tweets_paginated.prev_page,
        "is_following": is_following,
    }
