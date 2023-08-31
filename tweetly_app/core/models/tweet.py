from django.db import models
from .base import Base


class Tweet(Base):
    author = models.ForeignKey(to="CustomUser", on_delete=models.CASCADE, related_name='tweets')
    content = models.TextField(max_length=150)
    tags = models.ManyToManyField(to="Tag", through="TweetTag", through_fields=("tweet", "tag"))
    like = models.ManyToManyField(to='CustomUser', related_name='liked_tweets', through='TweetLike')
    comments = models.ManyToManyField(to='Comment', through='TweetComment', through_fields=("tweet", "comment"))

    class Meta:
        db_table = "tweets"
