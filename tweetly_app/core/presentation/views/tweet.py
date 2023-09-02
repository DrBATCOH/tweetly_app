from __future__ import annotations
from typing import TYPE_CHECKING

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required


if TYPE_CHECKING:
    from django.http import HttpRequest


from core.presentation.converters import convert_data_from_form_to_dto
from core.business_logic.services import create_tweet, get_tweet_by_id, get_tweets_by_tag
from core.presentation.forms import TweetForm
from core.business_logic.dto import TweetDTO, TagDTO
from core.models import Comment


@require_http_methods(request_method_list=["GET", "POST"])
@login_required
def add_tweet(request: HttpRequest) -> HttpResponse:

    if request.method == "GET":
        form = TweetForm()
        context = {"form": form, }
        return render(request=request, template_name="add_tweet.html", context=context)
    elif request.method == "POST":
        form = TweetForm(request.POST)
        context = {"form": form}
        if form.is_valid():
            data = convert_data_from_form_to_dto(TweetDTO, form.cleaned_data)
            create_tweet(data=data, author=request.user)
            return redirect("profile")


@login_required
@require_http_methods(request_method_list=["GET"])
def get_tweet(request: HttpRequest, tweet_id: int) -> HttpResponse:
    tweet = get_tweet_by_id(tweet_id=tweet_id)
    tweet.comment_count = Comment.objects.filter(tweet=tweet).count()
    context = {"tweet": tweet}
    return render(request=request, template_name="tweet.html", context=context)


@login_required
@require_http_methods(request_method_list=["GET"])
def tweet_by_tag(request: HttpRequest, tag_name) -> HttpResponse:
    tweets = get_tweets_by_tag(TagDTO(name=tag_name))
    context = {"tweets": tweets}
    return render(request=request, template_name="tweet_by_tag.html", context=context)
