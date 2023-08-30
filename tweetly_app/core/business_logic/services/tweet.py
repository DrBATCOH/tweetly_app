from __future__ import annotations

from typing import TYPE_CHECKING

from django.db import transaction
from django.db.models import Count, Q


if TYPE_CHECKING:
    from core.business_logic.dto import TweetDTO, SearchTweetDTO, TagDTO, TweetTagDTO
    from core.models import CustomUser

from core.models import Tweet, CustomUser, Tag
from .replace_swear_word import replace_swear_word_in_text
from core.business_logic.exceptions import TweetNotFound
from core.business_logic.dto import TweetTagDTO


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

        created_tweet = Tweet.objects.create(
            content=content,
            author=author
        )
        created_tweet.tags.set(tags_list)


def get_tweet_by_id(tweet_id: int) -> Tweet:
    try:
        tweet = Tweet.objects.annotate(
            like_count=Count("like"),
            retweet_count=Count("retweet"),
            comment_count=Count("comments")
        ).get(pk=tweet_id)
    except Tweet.DoesNotExist:
        raise TweetNotFound("Tweet does not exist.")
    return tweet


def search_tweet(data: SearchTweetDTO) -> list[Tweet]:
    tweets = Tweet.objects.select_related("author").prefetch_related("tags")

    if data.tags:
        tweets = tweets.filter(tags__name__icontains=data.tags)

    if data.author:
        author_query = Q(author__first_name__icontains=data.author) | Q(author__last_name__icontains=data.author)
        tweets = tweets.filter(author_query)

    tweets = tweets.order_by("-created_at")

    return list(tweets)


def get_tweets_by_tag(data: TagDTO) -> TweetTagDTO:

    tag = Tag.objects.get(name=data.name)
    tweets = (Tweet.objects.filter(tags=tag)
              .select_related("author")
              .annotate(like_count=Count("like"),
                        retweet_count=Count("retweet"),
                        comment_count=Count("comments"))
              .prefetch_related("like", "comments")
              .order_by("-created_at")
              )
    tag_tweet = TweetTagDTO(tag=tag, tweets=tweets)
    return tag_tweet
