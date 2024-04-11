from django.db import models

# Create your models here.
class TaskModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_done = models.BooleanField(default=False)
