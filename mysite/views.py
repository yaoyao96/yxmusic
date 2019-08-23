from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializers
# Create your views here.
 
class StudentViewSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
        queryset = Student.objects.all().order_by('-id')
    # 指定序列化的类
        serializer_class = StudentSerializers