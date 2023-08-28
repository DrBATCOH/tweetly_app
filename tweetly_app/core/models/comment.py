from django.db import models
from .base import Base


class Comment(Base):
    content = models.CharField(max_length=100)

    def __str__(self):
        return f'Comment by {self.user} on {self.tweet}'

    class Meta:
        db_table = "comments"
