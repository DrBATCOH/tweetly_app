from django.db import models
from .base import BaseModel
from core.models import CustomUser

class TweetModel(BaseModel):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField(max_length=150)
    count_likes = models.PositiveIntegerField(default=0)
    count_retweets = models.PositiveIntegerField(default=0)
    count_comments = models.PositiveIntegerField(default=0)


    class Meta:
        db_table = "tweets"
