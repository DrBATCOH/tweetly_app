from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.models import CustomUser

from core.models import Tweet, CustomUser
from core.business_logic.exceptions import SelfRetweetError


def retweet_tweet(user: CustomUser, tweet_id: int) -> None:
    tweet = Tweet.objects.select_related("author").prefetch_related("retweets").get(pk=tweet_id)
    
    if tweet.author == user:
        raise SelfRetweetError("You can't retweet your own tweet") 
    
    if user in tweet.retweets.all():
        tweet.retweets.remove(user)
    else:
        tweet.retweets.add(user)
