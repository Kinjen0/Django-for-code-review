from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    
    likes = models.ManyToManyField(User, related_name='liked_comments', blank=True)
    
