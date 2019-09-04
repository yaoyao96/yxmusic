
from rest_framework import serializers
from .models import Student, Teacher, StudentPaid, TeacherSalary, Income, Training
 
class StudentSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student     #model
        fields = ('url', 'id','name', 'level', 'date_of_birth', 'remarks','teacher', 'expired')   #field

class TeacherSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher     
        fields = ('url', 'id', 'name', 'expired')  

class StudentPaidSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentPaid     
        fields = ('url', 'id','number_of_course','amount','create_time','remarks', 'student') 

class TeacherSalarySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeacherSalary     
        fields = ('url', 'id','amount','year', 'month','remarks','teacher')

class IncomeSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Income     
        fields = ('url', 'id','amount','income_type','create_time','remarks') 

class TrainingSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Training    
        fields = ('url', 'id','number_of_month','amount','create_time','remarks','student') 

class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student     #model
        fields = ['id','name', 'level', 'date_of_birth', 'remarks','teacher', 'expired']   #field

class SalaryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherSalary     
        fields = ['id','year', 'month','amount','remarks','teacher']

class PaidListSerializer(serializers.Serializer):
    # class Meta:
    #     model = StudentPaid    
    #     fields = ['id','number_of_course','amount','create_time','remarks','student']
    id = serializers.IntegerField()
    number_of_course = serializers.IntegerField()
    amount = serializers.DecimalField(7,2)
    create_time = serializers.DateField()
    remarks = serializers.CharField()
    student = serializers.CharField()

class TrainingListSerializer(serializers.Serializer):
    # class Meta:
    #     model = Training    
    #     fields = ['id','number_of_month','amount','create_time','remarks','student']
    id = serializers.IntegerField()
    number_of_month = serializers.IntegerField()
    amount = serializers.DecimalField(7,2)
    create_time = serializers.DateField()
    remarks = serializers.CharField()
    student = serializers.CharField()

class paidPeriodSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    sum_of_paid = serializers.DecimalField(9,2)
    latest_paid_amount = serializers.DecimalField(7,2)
    latest_paid_course = serializers.IntegerField()
    latest_paid_time = serializers.DateField()
    duration = serializers.IntegerField()
    teacher = serializers.CharField()

class paidGroupByStudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    year = serializers.IntegerField()
    amount = serializers.DecimalField(9,2)    

class paidSumSerializer(serializers.Serializer):
    year = serializers.IntegerField()
    sumJan = serializers.DecimalField(9,2)
    sumFeb = serializers.DecimalField(9,2)
    sumMar = serializers.DecimalField(9,2)
    sumApr = serializers.DecimalField(9,2)
    sumMay = serializers.DecimalField(9,2)
    sumJun = serializers.DecimalField(9,2)
    sumJul = serializers.DecimalField(9,2)
    sumAug = serializers.DecimalField(9,2)
    sumSep = serializers.DecimalField(9,2)
    sumOct = serializers.DecimalField(9,2)
    sumNov = serializers.DecimalField(9,2)
    sumDec = serializers.DecimalField(9,2)
    sumYear = serializers.DecimalField(9,2)
