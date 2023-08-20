from django.db import models
from .customuser import CustomUser
from .base import BaseModel
from .tweet import TweetModel


class CommentModel(BaseModel):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, related_name='comments')
    tweet = models.ForeignKey(to=TweetModel, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=100)

    def __str__(self):
        return f'Comment by {self.user} on {self.tweet}'

    class Meta:
        db_table = "comments"
