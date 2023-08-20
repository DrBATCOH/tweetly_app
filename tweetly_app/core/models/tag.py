from django.db import models


class TagModel(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "tags"
