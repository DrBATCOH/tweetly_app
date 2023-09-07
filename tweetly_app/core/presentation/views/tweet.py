from __future__ import annotations

from typing import TYPE_CHECKING

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

if TYPE_CHECKING:
    from django.http import HttpRequest

from core.business_logic.dto import TweetDTO
from core.business_logic.services import (
    create_tweet,
    get_tweet_by_id,
    get_tweets_by_tag,
    comment_tweet
)
from core.models import Comment
from core.presentation.converters import convert_data_from_form_to_dto
from core.presentation.forms import TweetForm, CommentForm
from core.presentation.paginator import CustomPagination, PageNotExists


@require_http_methods(request_method_list=["GET", "POST"])
@login_required
def add_tweet(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = TweetForm()
        context = {
            "form": form,
        }
        return render(request=request, template_name="add_tweet.html", context=context)
    elif request.method == "POST":
        form = TweetForm(request.POST)
        context = {"form": form}
        if form.is_valid():
            data = convert_data_from_form_to_dto(TweetDTO, form.cleaned_data)
            create_tweet(data=data, author=request.user)
            return redirect("profile")

    return render(request, template_name="comment.html", context=context)


@login_required
@require_http_methods(request_method_list=["GET", "POST"])
def get_tweet_whit_comment(request: HttpRequest, tweet_id: int) -> HttpResponse:
    user = request.user
    tweet = get_tweet_by_id(tweet_id=tweet_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get("comment")
            comment_tweet(user, tweet_id, text)
            return redirect("tweet", tweet_id=tweet_id)
    else:
        form = CommentForm()

    tweet.comment_count = Comment.objects.filter(tweet=tweet).count()
    context = {"tweet": tweet, "form": form}
    return render(request=request, template_name="tweet.html", context=context)


@login_required
@require_http_methods(request_method_list=["GET"])
def tweet_by_tag(request: HttpRequest, tag_name: str) -> HttpResponse:
    tweet = get_tweets_by_tag(tag_name=tag_name)
    page_number = request.GET.get("page", 1)
    paginator = CustomPagination(per_page=5)
    try:
        tweets = paginator.paginate(data=tweet, page_number=page_number)
    except PageNotExists:
        raise HttpResponseBadRequest("Page doesn't exist.")
    context = {"tweets": tweets, "tag_name": tag_name}
    return render(request=request, template_name="tweet_by_tag.html", context=context)
