from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Course(models.Model): 
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=300,unique=True)
    description = models.TextField()
    credit = models.CharField(max_length=200)

    def __str__(self):
        return self.code
    
class Rating(models.Model):
    author = models.CharField(max_length=200,default="User")
    course = models.ForeignKey(Course, on_delete= models.CASCADE)
    stars = models.IntegerField()
    grade = models.CharField(max_length=200)
    difficulty = models.IntegerField()
    comment = models.TextField()
    date = models.DateField(default=timezone.now)
    anonymous = models.BooleanField(default = True)
    summary_word1=models.CharField(max_length=300,default="word1")
    summary_word2=models.CharField(max_length=300,default="word2")
    summary_word3=models.CharField(max_length=300,default="word3")
    
    def __str__(self):
        return self.comment