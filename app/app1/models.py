from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# THis model represents a single comment
class Comment(models.Model):
    # USer that made the comment
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Text content of the comment
    content = models.TextField()
    # Many to many field to hold the users who have liked the comments, can be zero(blank)
    likes = models.ManyToManyField(User, related_name='liked_comments', blank=True)
    
