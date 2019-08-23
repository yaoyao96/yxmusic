from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Student, Teacher, StudentPaid, TeacherSalary, Income, Training
from .serializers import StudentSerializers, TeacherSerializers, TeacherSalarySerializers, StudentPaidSerializers, IncomeSerializers, TrainingSerializers
# Create your views here.
 
class StudentViewSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
        queryset = Student.objects.all().order_by('-id')
    # 指定序列化的类
        serializer_class = StudentSerializers

class TeacherViewSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
        queryset = Teacher.objects.all().order_by('id')
    # 指定序列化的类
        serializer_class = TeacherSerializers

class StudentPaidViewSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
        queryset = StudentPaid.objects.all().order_by('id')
    # 指定序列化的类
        serializer_class = StudentPaidSerializers

class TeacherSalaryViewSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
        queryset = TeacherSalary.objects.all().order_by('id')
    # 指定序列化的类
        serializer_class = TeacherSalarySerializers

class IncomeViewSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
        queryset = Income.objects.all().order_by('id')
    # 指定序列化的类
        serializer_class = IncomeSerializers

class TrainingViewSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
        queryset = Training.objects.all().order_by('id')
    # 指定序列化的类
        serializer_class = TrainingSerializers