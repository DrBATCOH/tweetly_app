from django.db import models
from .base import BaseModel
from .customuser import CustomUser


class NotificationModel(BaseModel):
    message = models.CharField(max_length=255)
    is_real = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notifications')

    def __str__(self):
        return f'{self.user.username} - {self.message}'

    class Meta:
        db_table = "notifications"
