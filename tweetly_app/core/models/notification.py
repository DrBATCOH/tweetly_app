from django.db import models
from .base import Base


class Notification(Base):
    message = models.CharField(max_length=255)
    is_real = models.BooleanField(default=False)

    class Meta:
        db_table = "notifications"
