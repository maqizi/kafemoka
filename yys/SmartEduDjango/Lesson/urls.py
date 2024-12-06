from django.urls import path

from . import views

urlpatterns = [
    path("get_lesson_section/", views.Get_Lessson_Section.as_view(), name="get_lesson_section"),
]