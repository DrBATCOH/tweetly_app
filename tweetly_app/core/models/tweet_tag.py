from django.db import models
from .base import BaseModel
from .tag import TagModel
from .tweet import TweetModel


class TweetTags(BaseModel):
    tweet = models.ForeignKey(TweetModel, on_delete=models.CASCADE)
    tag = models.ForeignKey(TagModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"Tag '{self.tag}' on Tweet {self.tweet}"

    class Meta:
        db_table = "tweet_tag"
