from django.db import models
from .base import BaseModel
from .customuser import CustomUser



class EmailConfirmationCodes(BaseModel):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="codes",
    )
    code = models.CharField(max_length=100, unique=True)
    expiration = models.PositiveIntegerField()

    class Meta:
        db_table = "email_codes"