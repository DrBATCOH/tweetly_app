from django.contrib.auth.models import AbstractUser
from django.db import models
from .base import Base


class CustomUser(AbstractUser, Base):
    status = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=35, unique=True)
    avatar = models.ImageField(upload_to='media/users/avatars/', blank=True)
    country = models.CharField(max_length=100)
    birthdate = models.DateField(verbose_name="Birthdate")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "birthdate"]

    class Meta:
        db_table = "custom_user"


# обращение к ролям и разрешениям через мою кастомную модель а не через  group_set (что бы не было ошибки)
# CustomUser._meta.get_field('groups').remote_field.related_name = 'custom_users'
# CustomUser._meta.get_field('user_permissions').remote_field.related_name = 'custom_users'
