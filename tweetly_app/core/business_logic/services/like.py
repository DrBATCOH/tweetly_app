from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.models import CustomUser

from core.business_logic.exceptions import SelfLikeError
from core.models import Tweet

from .notification import create_notification


def add_like_by_tweet(user: CustomUser, tweet_id: int) -> None:
    tweet = Tweet.objects.get(pk=tweet_id)

    if tweet.author == user:
        raise SelfLikeError("You can't like yourself")

    if user in tweet.like.all():
        tweet.like.remove(user)
    else:
        tweet.like.add(user)
        message = f"{user.first_name} {user.last_name} liked your tweet: {tweet.content[0:20]}..."
        create_notification(recipient=tweet.author, message=message)
