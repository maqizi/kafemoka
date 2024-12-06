from django.core.paginator import Paginator, Page, EmptyPage
from django.db import models

# from Lesson.lesson_service import LessonPlanService


# from Lesson.lesson_service import LessonPlanService
# from Lesson.models import LessonPlan


class LessonPlanSectionService(models.Manager):
    # def __init__(self, *args, **kwargs):
    #     # 通过 __init__ 初始化 LessonPlanService 实例
    #     self.lesson_plan_service = LessonPlanService()
    #     super().__init__(*args, **kwargs)

    def create_section(self, lesson_plan_id, section_name, content):
        section = self.create(lesson_plan_id=lesson_plan_id, section_name=section_name, content=content)
        return section

    # 分页查询A教案的B部分的内容，默认查询1页，1页3条记录
    def get_content_paginated(self, lesson_title, section_name, page_size=3, page_num=1):
        from Lesson.models import LessonPlan
        lesson_plan_id = LessonPlan.objects.get_lesson_plan_id(lesson_title)
        sections = self.filter(lesson_plan_id=lesson_plan_id, section_name=section_name)

        paginator = Paginator(sections, page_size)

        return paginator;
