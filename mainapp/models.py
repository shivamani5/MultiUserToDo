from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    PRIORITY_CHOICES=[
        ("L", "Low"),
        ("M", "medium"),
        ("H", "High"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    title=models.CharField(max_length=400)
    description=models.TextField(max_length=1000)
    is_completed=models.BooleanField(default=False)
    priority=models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    due_date=models.DateField(blank=True, null=True)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
    

