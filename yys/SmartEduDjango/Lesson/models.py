from django.db import models

from Lesson.lesson_service import LessonPlanService
from Lesson.lesson_section_service import LessonPlanSectionService


# Create your models here.
class LessonPlan(models.Model):
    title = models.CharField(max_length=255)  # 教案标题
    content = models.TextField()  # 教案内容
    created_at = models.DateTimeField(auto_now_add=True)  # 创建时间
    updated_at = models.DateTimeField(auto_now=True)  # 更新时间

    objects = LessonPlanService()

class LessonPlanSection(models.Model):
    SECTION_CHOICES = [
        ('教学目标', '教学目标'),
        ('教学过程', '教学过程'),
        ('学情分析', '学情分析'),
        ('教学重难点', '教学重难点'),
        ('学习评价', '学习评价'),
        ('课后作业', '课后作业'),
    ]

    lesson_plan_id = models.IntegerField()  # 直接存储LessonPlan的id
    section_name = models.CharField(choices=SECTION_CHOICES, max_length=50)  # 板块名称
    content = models.TextField()  # 该板块的内容
    created_at = models.DateTimeField(auto_now_add=True)  # 创建时间
    updated_at = models.DateTimeField(auto_now=True)  # 更新时间

    objects = LessonPlanSectionService()