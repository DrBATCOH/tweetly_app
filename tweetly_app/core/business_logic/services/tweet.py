from __future__ import annotations

from typing import TYPE_CHECKING


from django.db.models import Count


if TYPE_CHECKING:
    from core.business_logic.dto import TweetDTO

from core.models import TweetModel


def create_tweet(data: TweetDTO) -> None:
    TweetModel.objects.create(
        autor=data.author,
        content=data.content,
        count_likes=data.count_likes,
        count_retweets=data.count_retweets,
        count_comments=data.count_comments
    )


# def get_tweet_by_id(tweet_id: int) -> TweetModel:
#     tweet: TweetModel = TweetModel.objects.annotate(like__count=Count("like__id")).get(pk=tweet_id)
#     return TweetModel
