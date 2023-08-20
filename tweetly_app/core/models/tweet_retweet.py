from django.db import models
from .base import BaseModel
from .retweet import RetweetModel
from .tweet import TweetModel


class TweetRetweet(BaseModel):
    tweet = models.ForeignKey(TweetModel, on_delete=models.CASCADE)
    retweet = models.ForeignKey(RetweetModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"Retweet '{self.tag}' on Tweet {self.tweet}"

    class Meta:
        db_table = "tweet_retweet"
