from django.db import models
from django.utils.text import slugify


class TaskModel(models.Model):
    name = models.TextField(unique=True)
    detail = models.TextField(null=True, blank=True)
    duration = models.DurationField()
    completed = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
