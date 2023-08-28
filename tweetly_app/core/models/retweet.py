from django.db import models
from .base import Base

class Retweet(Base):
    user = models.ForeignKey(to="CustomUser", on_delete=models.CASCADE)
    tweet = models.ForeignKey(to="Tweet", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} retweeted {self.tweet}"

    class Meta:
        db_table = "retweets"
