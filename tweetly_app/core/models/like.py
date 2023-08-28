from django.db import models
from .base import Base


class Like(Base):
    like_count = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.like_count}"
    

    class Meta:
        db_table = "likes"