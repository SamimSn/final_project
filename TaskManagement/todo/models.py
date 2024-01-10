from django.db import models
from django.contrib.auth.models import User

# Create your models here.
status = [
    ('Pending', 'Pending'),
    ('In Progress', 'In Progress'),
    ('Done', 'Done'),
]

class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)                                    # owner    
    title = models.CharField(max_length=100, blank=False)                                        # title
    description = models.TextField(blank=True)                                                   # description
    created_time = models.DateTimeField(auto_now_add=True)                                       # creation time
    updated_time = models.DateTimeField(auto_now=True)                                           # update time
    status = models.CharField(max_length=15, choices=status, null=False, default='Pending')      # status
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_time']
    
