from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=140)
    signature = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField()
    
    class Meta:
        ordering = ['-date']  # This sets default ordering for all queries
    
    def __str__(self):
        return self.title