"""
URL configuration for SmartEduDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.contrib import admin
from django.urls import re_path,path,include
# from . import views,testdb,search,search2
from Users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('Users.urls')), # demo user
    path('api/register/',views.Register.as_view()),
    path('api/login/',views.Login.as_view()),
    path('api/delect/',views.Delect.as_view()),

    path('api/insertlesson/',views.Insertlesson.as_view()),
    path('api/getLessondatas/',views.GetLessonDatas.as_view()),
    path('api/delectlessondata/',views.DelLessonData.as_view()),
    path('api/getLessondata/',views.GetLessonData.as_view()),
    path('api/resetLessondata/',views.ResetLessonData.as_view()),
    path('api/insertshare/',views.Insertshare.as_view()),
    path('api/getshare/',views.Getshare.as_view()),
    path('api/getdocuments/',views.GetTextSplitterDocuments.as_view()),
    path('api/uploadocuments/',views.uploadsFlie.as_view()),
    path('api/createdb/',views.createdb.as_view()),
    path('api/retrieve/',views.retrieve.as_view()),
    path('api/lesson/', include('Lesson.urls')),
]



