from __future__ import annotations

import uuid
import time

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from django.http import HttpRequest
    from core.business_logic.dto import ProfileDTO
    from core.models import CustomUser

from django.contrib.auth import get_user_model
from django.db.models import Q
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.core.mail import send_mail
from django.urls import reverse
from core.models import EmailConfirmationCodes
from django.conf import settings

from core.models import Follower, Tweet
from core.presentation.paginator import CustomPagination, PageNotExists
from .common import optimize_image, replace_file_name_to_uuid
from core.business_logic.exceptions import InvalidAuthCredentials


def get_user_profile(user_profile: get_user_model, page_number: int) -> dict[Any, Any]:
    last_login = user_profile.last_login
    is_online = (timezone.now() - last_login).seconds > 120
    tweets = Tweet.objects.filter(Q(author=user_profile) | Q(retweet__user=user_profile)).distinct().order_by("-created_at")
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
    is_online = (last_login - timezone.now()).seconds < 120
    tweets = Tweet.objects.filter(Q(author=author) | Q(retweet__user=author)).distinct().order_by("-created_at")
    page_number = request.GET.get("page", 1)
    paginator = CustomPagination(per_page=4)
    is_following = False

    if request.user.is_authenticated:
        is_following = Follower.objects.select_related('follower', 'following').filter(
            follower=request.user, following=author).exists()
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


def edit_user_profile(data: ProfileDTO, user: CustomUser) -> None:

    user = get_user_model().objects.get(pk=user.id)
    if data.avatar is not None:
        file = replace_file_name_to_uuid(data.avatar)
        file = optimize_image(file=file)
        user.avatar = file
    user.status = data.status
    user.first_name = data.first_name
    user.last_name = data.last_name
    user.username = data.username
    user.email = data.email
    user.country = data.country
    user.birthdate = data.birthdate
    user.save()
    if data.old_password and data.new_password:
        if user.check_password(data.old_password):
            user.set_password(data.new_password)
        else:
            raise InvalidAuthCredentials
    if user.email != data.email:
        user.is_active = False
        confirmation_code = str(uuid.uuid4())
        exp_time = int(time.time()) + settings.CONFIRMATION_CODE_LIFETIME
        EmailConfirmationCodes.objects.create(
            code=confirmation_code, user=user, expiration=exp_time
        )

        confirmation_url = (
            settings.SERVER_HOST + reverse("confirm-singup") + f"?code={confirmation_code}"
        )
        send_mail(
            subject="Confirn your email",
            message=f"Please confirm email by clicking the link below:\n\n{confirmation_url}",
            from_email=settings.EMAIL_FROM,
            recipient_list=[data.email],
        )
