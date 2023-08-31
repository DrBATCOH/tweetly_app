from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.models import CustomUser

from core.models import Tweet, CustomUser
from core.business_logic.exceptions import SelfLikeError


def add_like_by_tweet(user: CustomUser, tweet_id: int) -> None:
    tweet = Tweet.objects.get(pk=tweet_id)
    
    if tweet.author == user:
        raise SelfLikeError("You can't like yourself") 
    
    if user in tweet.like.all():
        tweet.like.remove(user)
    else:
        tweet.like.add(user)
