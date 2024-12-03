from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from Lesson.models import LessonPlanSection


# Create your views here.
class Get_Lessson_Section(APIView):

    def get(self, request):
        # 获取请求参数
        lesson_title = request.query_params.get('lesson_title')
        section_name = request.query_params.get('section_name')
        page_num = int(request.query_params.get('page_num', 1))  # 默认页码为1
        page_size = int(request.query_params.get('page_size', 10))  # 默认每页10条

        # 检查参数是否有效
        if not lesson_title or not section_name:
            return Response({"error": "lesson_title and section_name are required"}, status=status.HTTP_400_BAD_REQUEST)

        # 查询LessonPlanSection
        queryset = LessonPlanSection.objects.get_content_paginated(lesson_title, section_name, page_size, page_num)

        # 分页
        paginator = LessonPlanSection.objects.get_content_paginated(lesson_title, section_name, page_size, page_num)
        try:
            page = paginator.page(page_num)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)  # 如果页码超出范围，返回最后一页

        # 构建返回数据
        data = [
            {
                "content": section.content,
            }
            for section in page.object_list
        ]

        # 返回分页数据
        return Response({
            "total": paginator.count,  # 总条数
            "num_pages": paginator.num_pages,  # 总页数
            "current_page": page_num,  # 当前页码
            "results": data  # 当前页的查询结果
        }, status=status.HTTP_200_OK)