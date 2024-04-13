from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=5)
    completed = models.BooleanField(default=False,blank=True,null=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
