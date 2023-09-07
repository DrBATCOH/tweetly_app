from __future__ import annotations

from typing import TYPE_CHECKING

from django.db import transaction
from django.db.models import Count, Q

if TYPE_CHECKING:
    from core.business_logic.dto import TweetDTO, SearchTweetDTO
    from core.models import CustomUser


from core.business_logic.exceptions import TweetNotFound
from core.models import Comment, Tag, Tweet
from .replace_swear_word import replace_swear_word_in_text


def create_tweet(data: TweetDTO, author: CustomUser) -> None:
    content = replace_swear_word_in_text(data.content)
    with transaction.atomic():
        tags: list[str] = data.tags.split("\r\n")
        tags_list: list[Tag] = []
        for tag in tags:
            tag = tag.lower()
            try:
                tags_from_db = Tag.objects.get(name=tag)
            except Tag.DoesNotExist:
                tags_from_db = Tag.objects.create(name=tag)
            tags_list.append(tags_from_db)

        created_tweet = Tweet.objects.create(content=content, author=author)
        created_tweet.tags.set(tags_list)


def get_tweet_by_id(tweet_id: int) -> Tweet:
    try:
        tweet = Tweet.objects.annotate(
            like_count=Count("like"),
            retweet_count=Count("retweet"),
            comment_count=Count("comments"),
        ).get(pk=tweet_id)
    except Tweet.DoesNotExist:
        raise TweetNotFound("Tweet does not exist.")
    return tweet


def search_tweet(data: SearchTweetDTO) -> list[Tweet]:
    tweets = Tweet.objects.select_related("author").prefetch_related("tags")

    if data.tags:
        tweets = tweets.filter(tags__name__icontains=data.tags)

    if data.author:
        author_query = Q(author__first_name__icontains=data.author) | Q(
            author__last_name__icontains=data.author
        )
        tweets = tweets.filter(author_query)

    tweets = tweets.order_by("-created_at")

    return list(tweets)


def get_tweets_by_tag(tag_name: str) -> list[Tweet]:
    tag = Tag.objects.get(name=tag_name)
    tweet = (Tweet.objects.filter(tags=tag)
             .select_related("author")
             .annotate(
                 like_count=Count("like"),
                 retweet_count=Count("retweet"),
                 comment_count=Count("comments"),
    )
        .prefetch_related("like", "comments")
        .order_by("-created_at")
    )
    return tweet


def calculate_comment_counts(tweets):
    for tweet in tweets:
        tweet.comment_count = Comment.objects.filter(tweet=tweet).count()
