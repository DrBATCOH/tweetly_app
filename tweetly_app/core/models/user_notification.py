from django.db import models
from .base import Base


class UserNotification(Base):
    user = models.ForeignKey(to="CustomUser", on_delete=models.CASCADE)
    notification = models.ForeignKey(to="Notification", on_delete=models.CASCADE)

    class Meta:
        db_table = "users_notifications"
