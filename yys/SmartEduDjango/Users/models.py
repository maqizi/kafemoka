from django.db import models

# Create your models here.
class Users(models.Model):
    user = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)

class Lesson(models.Model):
    UserName = models.CharField(max_length=30)
    LessonName = models.CharField(max_length=30)
    Navigation = models.TextField()             # 导航
    Lessoncontent = models.TextField()          # 课程内容

class Share(models.Model):
    Author = models.CharField(max_length=30)
    Sharer = models.CharField(max_length=30)
    Privilege = models.TextField()             
    Lessonid = models.TextField()         
    


