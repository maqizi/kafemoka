from django.db import models

class LessonPlanService(models.Manager):

    def get_lesson_plan_id(self, lesson_plan_title):
        lesson_plan = self.filter(title=lesson_plan_title).first()
        return lesson_plan.id

    def create_lesson_plan(self, lesson_plan_title):
        lesson_plan = self.filter(title=lesson_plan_title)
        if not lesson_plan:
            lesson_plan = self.create(title=lesson_plan_title)
            print("创建成功")




