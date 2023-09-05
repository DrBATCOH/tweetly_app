from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.models import CustomUser

from core.business_logic.exceptions import SelfRetweetError
from core.models import Tweet

from .notification import create_notification


def retweet_tweet(user: CustomUser, tweet_id: int) -> None:
    tweet = (
        Tweet.objects.select_related("author")
        .prefetch_related("retweets")
        .get(pk=tweet_id)
    )

    if tweet.author == user:
        raise SelfRetweetError("You can't retweet your own tweet")

    if user in tweet.retweets.all():
        tweet.retweets.remove(user)
    else:
        tweet.retweets.add(user)
        message = f"{user.first_name} {user.last_name} retweeted your tweet"
        create_notification(recipient=tweet.author, message=message)
