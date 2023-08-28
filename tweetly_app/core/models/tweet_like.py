from django.db import models
from .base import Base


class TweetLike(Base):
    tweet = models.ForeignKey(to="Tweet", on_delete=models.CASCADE)
    like = models.ForeignKey(to="Like", on_delete=models.CASCADE)

    class Meta:
        db_table = "tweet_like"
