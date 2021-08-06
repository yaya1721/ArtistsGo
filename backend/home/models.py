from django.db import models
from django.utils import timezone
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255)  #author
    netid = models.CharField(max_length=10,unique=True, null=True)

class Post(models.Model):
    author = models.CharField(max_length=20) 
    create_date = models.DateField(default=timezone.now)  #time posted
    category = models.CharField(max_length=255) 
    title = models.CharField(max_length=200)
    description = models.TextField()  
    content = models.ImageField(max_length=255) 

    #completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title