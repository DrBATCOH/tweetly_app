from __future__ import annotations

from typing import TYPE_CHECKING

from core.models import Comment, Tweet, TweetComment

from .replace_swear_word import replace_swear_word_in_text

if TYPE_CHECKING:
    from core.models import CustomUser


def comment_tweet(user: CustomUser, tweet_id: int, text: str) -> None:
    if not text.strip():
        raise ValueError("Comment text cannot be empty.")
    format_text = replace_swear_word_in_text(text)
    tweet = Tweet.objects.get(pk=tweet_id)
    comment = Comment(user=user, content=format_text)
    comment.save()

    tweet_comment = TweetComment(tweet=tweet, comment=comment)
    tweet_comment.save()
