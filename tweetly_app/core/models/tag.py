from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "tags"
