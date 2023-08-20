from django.db import models
from .base import BaseModel
from .customuser import CustomUser


class FollowerModel(BaseModel):
    follower = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='following')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.follower} follows {self.user}'

    class Meta:
        db_table = "followers"
