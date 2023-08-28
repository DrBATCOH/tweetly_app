from django.db import models
from .base import Base


class TweetComment(Base):
    tweet = models.ForeignKey(to="Tweet", on_delete=models.CASCADE, related_name='tweets')
    comment = models.ForeignKey(to="Comment", on_delete=models.CASCADE, related_name='comments')

    class Meta:
        db_table = "tweet_comment"
