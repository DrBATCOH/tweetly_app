from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to="media/avatars/")
    country = models.CharField(max_length=100)
    birthdate = models.DateField(verbose_name="Birthdate")

    class Meta:
        db_table = "custom_user"


CustomUser._meta.get_field('groups').remote_field.related_name = 'custom_users'
CustomUser._meta.get_field('user_permissions').remote_field.related_name = 'custom_users'
