from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from .serializers import TeacherSerializer, CategorySerializer, CourseSerializer, ChapterSerializer
from . import models


class TeacherList(generics.ListCreateAPIView):
   queryset = models.Teacher.objects.all()
   serializer_class = TeacherSerializer
   # permission_classes = [permissions.IsAuthenticated]  
   
class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = models.Teacher.objects.all()
   serializer_class = TeacherSerializer
   # permission_classes = [permissions.IsAuthenticated] 

@csrf_exempt
def teacher_login(request):
    email = request.POST['email']
    password = request.POST['password']
    try:
        teacherData = models.Teacher.objects.get(email=email, password=password)
    except models.Teacher.DoesNotExist:
        teacherData = None
    if teacherData:
        return JsonResponse({'bool': True, 'teacher_id': teacherData.id})
    else:
        return JsonResponse({'bool': False})


class CategoryList(generics.ListCreateAPIView):
   queryset = models.CourseCategory.objects.all()
   serializer_class = CategorySerializer
   # permission_classes = [permissions.IsAuthenticated] 
   
#   Course 
class CourseList(generics.ListCreateAPIView):
   queryset = models.Course.objects.all()
   serializer_class = CourseSerializer
   # permission_classes = [permissions.IsAuthenticated] 
   def get_queryset(self):
    qs = super().get_queryset()  # Get the default queryset
    if 'result' in self.request.GET:
        limit = int(self.request.GET["result"])
        # If 'result' is in the GET parameters, return a filtered and sliced queryset
        qs = models.Course.objects.all().order_by('-id')[:4]
    return qs

#   Specific Teacher course
class TeacherCourseList(generics.ListCreateAPIView):
   serializer_class = CourseSerializer
   # permission_classes = [permissions.IsAuthenticated] 
   
   def get_queryset(self):
      teacher_id = self.kwargs['teacher_id']
      teacher = models.Teacher.objects.get(pk=teacher_id)
      return models.Course.objects.filter(teacher = teacher)


# Chapter
class ChapterList(generics.ListCreateAPIView):
    queryset = models.Chapter.objects.all()
    serializer_class = ChapterSerializer
# Chapter
class CourseChapterList(generics.ListAPIView):
    serializer_class = ChapterSerializer
    def get_queryset(self):
      course_id = self.kwargs['course_id']
      course = models.Course.objects.get(pk=course_id)
      return models.Chapter.objects.filter(course = course)


# Chapter Detail
class ChapterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Chapter.objects.all()
    serializer_class = ChapterSerializer
    # permission_classes = [permissions.IsAuthenticated]  # Uncomment to enforce authentication

class TeacherCourseDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = models.Course.objects.all()
   serializer_class = CourseSerializer
    
   # permission_classes = [permissions.IsAuthenticated] 
   
   