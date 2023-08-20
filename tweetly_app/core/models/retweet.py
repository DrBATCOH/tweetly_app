from django.db import models
from .base import BaseModel
from .customuser import CustomUser
from .tweet import TweetModel


class RetweetModel(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tweet = models.ForeignKey(TweetModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} retweeted {self.tweet}"

    class Meta:
        db_table = "retweet"
