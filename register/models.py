from django.db import models
from categories.models import Category
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Category, related_name='posts')  
    register = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')  
    def __str__(self):
        return self.title
