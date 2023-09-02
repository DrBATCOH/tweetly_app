from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.models import CustomUser

from core.models import TweetComment, CustomUser, Comment, Tweet


def comment_tweet(user: CustomUser, tweet_id: int, text: str) -> None:
    if not text.strip():
        raise ValueError("Comment text cannot be empty.")
    
    tweet = Tweet.objects.get(pk=tweet_id)
    comment = Comment(user=user, content=text)
    comment.save()
    
    tweet_comment = TweetComment(tweet=tweet, comment=comment)
    tweet_comment.save()



