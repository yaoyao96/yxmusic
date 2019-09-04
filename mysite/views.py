from django.shortcuts import render,get_object_or_404

# Create your views here.
from rest_framework import viewsets
from django.db.models import F, Sum
from datetime import date
from decimal import Decimal
from .models import Student, Teacher, StudentPaid, TeacherSalary, Income, Training
from .serializers import paidGroupByStudentSerializer, paidSumSerializer, StudentListSerializer, paidPeriodSerializer, SalaryListSerializer,PaidListSerializer,TrainingListSerializer,StudentSerializers, TeacherSerializers, TeacherSalarySerializers, StudentPaidSerializers, IncomeSerializers, TrainingSerializers
# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.response import Response

 
class StudentViewSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
        queryset = Student.objects.all().filter(expired=False).order_by('id')
    # 指定序列化的类
        serializer_class = StudentSerializers

class TeacherViewSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
        queryset = Teacher.objects.all().filter(expired=False).order_by('id')
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
        queryset = Income.objects.all().order_by('-id')
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

class paidYear: 
   def __init__(self, year, sumJan, sumFeb, sumMar, sumApr, sumMay, sumJun, sumJul, sumAug, sumSep, sumOct, sumNov, sumDec, sumYear):
      self.year = year
      self.sumJan = sumJan
      self.sumFeb = sumFeb
      self.sumMar = sumMar
      self.sumApr = sumApr
      self.sumMay = sumMay
      self.sumJun = sumJun
      self.sumJul = sumJul
      self.sumAug = sumAug
      self.sumSep = sumSep
      self.sumOct = sumOct
      self.sumNov = sumNov
      self.sumDec = sumDec
      self.sumYear = sumYear

class paidGroup:
    def __init__(self, id, name, year, amount):
        self.id = id
        self.name = name
        self.year = year
        self.amount = amount
   
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

def deleteTeacherForStudent(request, tid):
    t = get_object_or_404(Teacher,pk=tid)
    # '空' id为6
    t_blank = get_object_or_404(Teacher,pk=6)
    studentList = Student.objects.all().filter(teacher=t)
    if(len(studentList)>0):
        for s in studentList:
            s.teacher = t_blank
            s.save()
    serializer = StudentListSerializer(studentList, many=True)
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
    studentList = Student.objects.all().filter(expired=False).order_by('id')
    paidPeriodList = []
    for s in studentList:
        id = s.id
        sum_of_paid = StudentPaid.objects.filter(student=s).aggregate(Sum('amount'))
        # if(sum_of_paid):
        #     sum_of_paid=0
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
        pp= paidSum(id, name, sum_of_paid['amount__sum'], latest_paid_amount, latest_paid_course, latest_paid_time, duration, teacher)
        paidPeriodList.append(pp)
    serializer = paidPeriodSerializer(paidPeriodList, many=True)
    return JsonResponse(serializer.data, safe=False)

def paidSumList(request):
    sumList = []
    if len(StudentPaid.objects.all()) > 0:
         latest_paid = StudentPaid.objects.order_by('-create_time')[0]
         earliest_paid = StudentPaid.objects.order_by('create_time')[0]
         max_year = latest_paid.create_time.year
         min_year = earliest_paid.create_time.year
    else:
        serializer = paidSumSerializer(sumList, many=True)
        return JsonResponse(serializer.data, safe=False)
    i = min_year
    while i <= max_year:
        year = i
        # paid
        sumJanPaid = StudentPaid.objects.filter(create_time__year = i, create_time__month = 1).aggregate(Sum('amount'))
        sumFebPaid = StudentPaid.objects.filter(create_time__year = i, create_time__month = 2).aggregate(Sum('amount'))
        sumMarPaid = StudentPaid.objects.filter(create_time__year = i, create_time__month = 3).aggregate(Sum('amount'))
        sumAprPaid = StudentPaid.objects.filter(create_time__year = i, create_time__month = 4).aggregate(Sum('amount'))
        sumMayPaid = StudentPaid.objects.filter(create_time__year = i, create_time__month = 5).aggregate(Sum('amount'))
        sumJunPaid = StudentPaid.objects.filter(create_time__year = i, create_time__month = 6).aggregate(Sum('amount'))
        sumJulPaid = StudentPaid.objects.filter(create_time__year = i, create_time__month = 7).aggregate(Sum('amount'))
        sumAugPaid = StudentPaid.objects.filter(create_time__year = i, create_time__month = 8).aggregate(Sum('amount'))
        sumSepPaid = StudentPaid.objects.filter(create_time__year = i, create_time__month = 9).aggregate(Sum('amount'))
        sumOctPaid = StudentPaid.objects.filter(create_time__year = i, create_time__month = 10).aggregate(Sum('amount'))
        sumNovPaid = StudentPaid.objects.filter(create_time__year = i, create_time__month = 11).aggregate(Sum('amount'))
        sumDecPaid = StudentPaid.objects.filter(create_time__year = i, create_time__month = 12).aggregate(Sum('amount'))
        sumYearPaid = StudentPaid.objects.filter(create_time__year = i).aggregate(Sum('amount'))

        py = paidYear(year, sumJanPaid['amount__sum'], sumFebPaid['amount__sum'], sumMarPaid['amount__sum'], sumAprPaid['amount__sum'], sumMayPaid['amount__sum'], sumJunPaid['amount__sum'], 
        sumJulPaid['amount__sum'], sumAugPaid['amount__sum'], sumSepPaid['amount__sum'], sumOctPaid['amount__sum'], sumNovPaid['amount__sum'], sumDecPaid['amount__sum'], sumYearPaid['amount__sum'])
        
        for item in py.__dict__.items():
            if(item[1] is None):
                setattr(py,item[0],0)
        sumList.append(py)
        i +=1
    serializer = paidSumSerializer(sumList, many=True)
    return JsonResponse(serializer.data, safe=False)

def trainingSumList(request):
    sumList = []
    if len(Training.objects.all()) > 0:
         latest_training = Training.objects.order_by('-create_time')[0]
         earliest_training = Training.objects.order_by('create_time')[0]
         max_year = latest_training.create_time.year
         min_year = earliest_training.create_time.year
    else:
        serializer = paidSumSerializer(sumList, many=True)
        return JsonResponse(serializer.data, safe=False)
    i = min_year
    while i <= max_year:
        year = i
        # Training
        sumJanTraining = Training.objects.filter(create_time__year = i, create_time__month = 1).aggregate(Sum('amount'))
        sumFebTraining = Training.objects.filter(create_time__year = i, create_time__month = 2).aggregate(Sum('amount'))
        sumMarTraining = Training.objects.filter(create_time__year = i, create_time__month = 3).aggregate(Sum('amount'))
        sumAprTraining = Training.objects.filter(create_time__year = i, create_time__month = 4).aggregate(Sum('amount'))
        sumMayTraining = Training.objects.filter(create_time__year = i, create_time__month = 5).aggregate(Sum('amount'))
        sumJunTraining = Training.objects.filter(create_time__year = i, create_time__month = 6).aggregate(Sum('amount'))
        sumJulTraining = Training.objects.filter(create_time__year = i, create_time__month = 7).aggregate(Sum('amount'))
        sumAugTraining = Training.objects.filter(create_time__year = i, create_time__month = 8).aggregate(Sum('amount'))
        sumSepTraining = Training.objects.filter(create_time__year = i, create_time__month = 9).aggregate(Sum('amount'))
        sumOctTraining = Training.objects.filter(create_time__year = i, create_time__month = 10).aggregate(Sum('amount'))
        sumNovTraining = Training.objects.filter(create_time__year = i, create_time__month = 11).aggregate(Sum('amount'))
        sumDecTraining = Training.objects.filter(create_time__year = i, create_time__month = 12).aggregate(Sum('amount'))
        sumYearTraining = Training.objects.filter(create_time__year = i).aggregate(Sum('amount'))
        py = paidYear(year, sumJanTraining['amount__sum'], sumFebTraining['amount__sum'], sumMarTraining['amount__sum'], sumAprTraining['amount__sum'], sumMayTraining['amount__sum'], sumJunTraining['amount__sum'], 
        sumJulTraining['amount__sum'], sumAugTraining['amount__sum'], sumSepTraining['amount__sum'], sumOctTraining['amount__sum'], sumNovTraining['amount__sum'], sumDecTraining['amount__sum'], sumYearTraining['amount__sum'])
        for item in py.__dict__.items():
            if(item[1] is None):
                setattr(py,item[0],0)
        sumList.append(py)
        i +=1
    serializer = paidSumSerializer(sumList, many=True)
    return JsonResponse(serializer.data, safe=False)

def StudentPaidList(request):
    spList = StudentPaid.objects.all()
    serializer = PaidListSerializer(spList, many=True)
    return JsonResponse(serializer.data, safe=False)

def TrainingList(request):
    tList = Training.objects.all()
    serializer = TrainingListSerializer(tList, many=True)
    return JsonResponse(serializer.data, safe=False)

def PaidGroudByStudent(request):
    sList = Student.objects.all()
    pgList =[]
    j = 1
    for s in sList:
        name = s.name
        if(len(StudentPaid.objects.filter(student=s))>0):
            max_year = StudentPaid.objects.filter(student=s).order_by('-create_time')[0].create_time.year
            min_year = StudentPaid.objects.filter(student=s).order_by('create_time')[0].create_time.year
            i = min_year
            while i <= max_year:
                sumYear = StudentPaid.objects.filter(create_time__year = i, student = s).aggregate(Sum('amount'))
                pgbs = paidGroup(j,name,i,sumYear['amount__sum'])
                j += 1
                pgList.append(pgbs)
                i += 1
    serializer = paidGroupByStudentSerializer(pgList, many=True)
    return JsonResponse(serializer.data, safe=False)

def TrainingGroudByStudent(request):
    sList = Student.objects.all()
    pgList =[]
    j = 1
    for s in sList:
        name = s.name
        if(len(Training.objects.filter(student=s))>0):
            max_year = Training.objects.filter(student=s).order_by('-create_time')[0].create_time.year
            min_year = Training.objects.filter(student=s).order_by('create_time')[0].create_time.year
            i = min_year
            while i <= max_year:
                sumYear = Training.objects.filter(create_time__year = i, student = s).aggregate(Sum('amount'))
                pgbs = paidGroup(j,name,i,sumYear['amount__sum'])
                j += 1
                pgList.append(pgbs)
                i += 1
    serializer = paidGroupByStudentSerializer(pgList, many=True)
    return JsonResponse(serializer.data, safe=False)




