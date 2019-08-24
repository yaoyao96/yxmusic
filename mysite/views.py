from django.shortcuts import render,get_object_or_404

# Create your views here.
from rest_framework import viewsets
from .models import Student, Teacher, StudentPaid, TeacherSalary, Income, Training
from .serializers import SalaryListSerializer,PaidListSerializer,TrainingListSerializer,StudentSerializers, TeacherSerializers, TeacherSalarySerializers, StudentPaidSerializers, IncomeSerializers, TrainingSerializers
# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
 
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

@csrf_exempt
def salaryListByTeacherId(request,tid):
    t = get_object_or_404(Teacher,pk=tid)
    # salaryList = TeacherSalary.objects.all()
    salaryList = TeacherSalary.objects.filter(teacher=t).order_by('-month')
    serializer = SalaryListSerializer(salaryList, many=True)
    return JsonResponse(serializer.data, safe=False)

def salaryListByTeacherIdAndYear(request,tid,y):
    t = get_object_or_404(Teacher,pk=tid)
    # salaryList = TeacherSalary.objects.all()
    sList = TeacherSalary.objects.filter(teacher=t)
    salaryList = sList.filter(year=y).order_by('-month')
    serializer = SalaryListSerializer(salaryList, many=True)
    return JsonResponse(serializer.data, safe=False)

def paidListByStudentId(request,sid):
    s = get_object_or_404(Student,pk=sid)
    # salaryList = TeacherSalary.objects.all()
    paidList = StudentPaid.objects.filter(student=s).order_by('-create_time')
    serializer = PaidListSerializer(paidList, many=True)
    return JsonResponse(serializer.data, safe=False)

def trainingListByStudentId(request,sid):
    s = get_object_or_404(Student,pk=sid)
    # salaryList = TeacherSalary.objects.all()
    trainingList = Training.objects.filter(student=s).order_by('-create_time')
    serializer = TrainingListSerializer(trainingList, many=True)
    return JsonResponse(serializer.data, safe=False)