from django.db import models

from .base import Base


class Follower(Base):
    follower = models.ForeignKey(
        to="CustomUser", on_delete=models.CASCADE, related_name="following"
    )
    following = models.ForeignKey(
        to="CustomUser", on_delete=models.CASCADE, related_name="follower"
    )

    class Meta:
        db_table = "followers"
        unique_together = ("follower", "following")
