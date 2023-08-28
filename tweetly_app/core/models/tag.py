from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True, blank=True)

    class Meta:
        db_table = "tags"
