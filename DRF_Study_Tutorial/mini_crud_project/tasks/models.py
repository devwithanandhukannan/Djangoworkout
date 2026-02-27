from django.db import models


class Task(models.Model):
    # Title is required and helps identify the task quickly.
    title = models.CharField(max_length=120)
    # Description is optional extra detail.
    description = models.TextField(blank=True)
    # This flag marks whether the task is complete.
    is_done = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

