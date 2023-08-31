from __future__ import annotations

import logging
from typing import TYPE_CHECKING
from core.business_logic.services import add_like_by_tweet
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods
from core.business_logic.exceptions import SelfLikeError

if TYPE_CHECKING:
    from django.http import HttpRequest


@require_http_methods(request_method_list=["POST", "GET"])
def like_tweet(request: HttpRequest, tweet_id: int) -> HttpResponse:
    user = request.user
    try:
        add_like_by_tweet(user, tweet_id)
        return redirect(to=request.META.get("HTTP_REFERER"))
    except SelfLikeError as err:
        error_message = str(err)
        return redirect(request.META.get("HTTP_REFERER"), {"error_message": error_message})
