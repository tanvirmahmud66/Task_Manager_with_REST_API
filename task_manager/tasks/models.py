from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# tasks models

class Tasks(models.Model):
    PRIORITY_CHOICES = [
        ('a', 'Low'),
        ('b', 'Medium'),
        ('c', 'High'),
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    complete = models.BooleanField(default=False)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-priority']
        verbose_name = "Tasks Table"
        verbose_name_plural = "Tasks Table"

    def __str__(self):
        return self.title
    

class Photos(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='task_photos/')

    class Meta:
        verbose_name = "Task's Photo Table"
        verbose_name_plural = "Task's Photo Table"

    def __str__(self):
        return str(self.image)



