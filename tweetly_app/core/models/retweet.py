from django.db import models
from .base import Base


class Retweet(Base):
    user = models.ForeignKey(to="CustomUser", on_delete=models.CASCADE)
    tweet = models.ForeignKey(to="Tweet", on_delete=models.CASCADE)

    class Meta:
        db_table = "retweets"
