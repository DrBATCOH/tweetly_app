from django.db import models

from .base import Base


class TweetTag(Base):
    tweet = models.ForeignKey(to="Tweet", on_delete=models.CASCADE)
    tag = models.ForeignKey(to="Tag", on_delete=models.CASCADE)

    class Meta:
        db_table = "tweet_tag"
