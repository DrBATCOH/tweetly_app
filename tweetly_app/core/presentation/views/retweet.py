from __future__ import annotations

from typing import TYPE_CHECKING

from core.business_logic.exceptions import SelfRetweetError
from core.business_logic.services import retweet_tweet
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods

if TYPE_CHECKING:
    from django.http import HttpRequest


@require_http_methods(request_method_list=["POST", "GET"])
def make_retweet(request: HttpRequest, tweet_id: int) -> HttpResponse:
    user = request.user
    try:
        retweet_tweet(user, tweet_id)
        return redirect(to=request.META.get("HTTP_REFERER"))
    except SelfRetweetError as err:
        error_message = str(err)
        return redirect(
            request.META.get("HTTP_REFERER"), {"error_message": error_message}
        )
