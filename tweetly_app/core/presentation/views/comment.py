from __future__ import annotations

from typing import TYPE_CHECKING
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.db.models import Count


from core.business_logic.services import comment_tweet
from core.presentation.forms import CommentForm
from core.models import Tweet


if TYPE_CHECKING:
    from django.http import HttpRequest


@require_http_methods(request_method_list=["POST", "GET"])
def add_comment(request: HttpRequest, tweet_id: int) -> HttpResponse:
    user = request.user
    tweet = get_object_or_404(Tweet, pk=tweet_id)

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('comment')
            comment_tweet(user, tweet_id, text)
            return redirect('tweet', tweet_id=tweet_id)

    tweet = Tweet.objects.annotate(comment_count=Count('comments')).get(pk=tweet_id)

    context = {"tweet": tweet, "form": form}
    return render(request, template_name="tweet.html", context=context)
