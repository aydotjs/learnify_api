from rest_framework import serializers
from . import models

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields=["id","full_name", "email", "password", "qualification", "mobile_no",]
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields=["id", "title", "description"]
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields=["id", "category", "teacher", "title", "description", "featured_img", "languages"]
        
class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chapter
        fields = ['id', 'course', 'title', 'description', 'video', 'remarks']

        