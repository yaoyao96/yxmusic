from django.shortcuts import render,get_object_or_404

# Create your views here.
from rest_framework import viewsets
from django.db.models import F, Sum
from datetime import date
from .models import Student, Teacher, StudentPaid, TeacherSalary, Income, Training
from .serializers import paidPeriodSerializer, SalaryListSerializer,PaidListSerializer,TrainingListSerializer,StudentSerializers, TeacherSerializers, TeacherSalarySerializers, StudentPaidSerializers, IncomeSerializers, TrainingSerializers
# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
 
class StudentViewSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
        queryset = Student.objects.all().order_by('id')
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

class paidSum: 
   def __init__(self, id, name, sum_of_paid, latest_paid_amount, latest_paid_course, latest_paid_time, duration, teacher):
      self.id = id
      self.sum_of_paid = sum_of_paid
      self.name = name
      self.latest_paid_amount = latest_paid_amount
      self.latest_paid_course = latest_paid_course
      self.latest_paid_time = latest_paid_time
      self.duration = duration
      self.teacher = teacher

   
#    def displayCount(self):
#      print "Total Employee %d" % Employee.empCount
 
#    def displayEmployee(self):
#       print "Name : ", self.name,  ", Salary: ", self.salary

@csrf_exempt
def salaryListByTeacherId(request,tid):
    t = get_object_or_404(Teacher,pk=tid)
    # salaryList = TeacherSalary.objects.all()
    salaryList = TeacherSalary.objects.filter(teacher=t).order_by('-id').order_by('-month').order_by('-year')
    serializer = SalaryListSerializer(salaryList, many=True)
    return JsonResponse(serializer.data, safe=False)

def salaryListByTeacherIdAndYear(request,tid,y):
    t = get_object_or_404(Teacher,pk=tid)
    # salaryList = TeacherSalary.objects.all()
    sList = TeacherSalary.objects.filter(teacher=t)
    salaryList = sList.filter(year=y).order_by('-month').order_by('-id')
    serializer = SalaryListSerializer(salaryList, many=True)
    return JsonResponse(serializer.data, safe=False)

def paidListByStudentId(request,sid):
    s = get_object_or_404(Student,pk=sid)
    # salaryList = TeacherSalary.objects.all()
    paidList = StudentPaid.objects.filter(student=s).order_by('-create_time').order_by('-id')
    serializer = PaidListSerializer(paidList, many=True)
    return JsonResponse(serializer.data, safe=False)

def trainingListByStudentId(request,sid):
    s = get_object_or_404(Student,pk=sid)
    # salaryList = TeacherSalary.objects.all()
    trainingList = Training.objects.filter(student=s).order_by('-create_time').order_by('-id')
    serializer = TrainingListSerializer(trainingList, many=True)
    return JsonResponse(serializer.data, safe=False)

def paidPeriod(request):
    studentList = Student.objects.all().order_by('id')
    paidPeriodList = []
    for s in studentList:
        id = s.id
        sum_of_paid = StudentPaid.objects.filter(student=s).aggregate(Sum('amount'))
        if(sum_of_paid):
            sum_of_paid=0
        name = s.name
        latest_paid_list = StudentPaid.objects.filter(student=s).order_by('-id')
        if(len(latest_paid_list)>0):
            latest_paid = latest_paid_list[0]
            latest_paid_amount = latest_paid.amount
            latest_paid_course = latest_paid.number_of_course
            latest_paid_time = latest_paid.create_time
        else:
            latest_paid_amount = 0
            latest_paid_course = 0
            latest_paid_time = date(2000,1,1)
        duration = (date.today() - latest_paid_time).days
        teacher = s.teacher.name
        pp= paidSum(id, name, sum_of_paid, latest_paid_amount, latest_paid_course, latest_paid_time, duration, teacher)
        paidPeriodList.append(pp)
    serializer = paidPeriodSerializer(paidPeriodList, many=True)
    return JsonResponse(serializer.data, safe=False)