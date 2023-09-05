from django.db import models

from .base import Base


class Notification(Base):
    message = models.CharField(max_length=255)

    class Meta:
        db_table = "notifications"
