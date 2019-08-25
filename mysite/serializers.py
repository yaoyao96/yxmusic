
from rest_framework import serializers
from .models import Student, Teacher, StudentPaid, TeacherSalary, Income, Training
 
class StudentSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student     #model
        fields = ('url', 'id','name', 'level', 'date_of_birth', 'remarks','teacher')   #field

class TeacherSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher     
        fields = ('url', 'id', 'name')  

class StudentPaidSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentPaid     
        fields = ('url', 'id','number_of_course','amount','create_time','student') 

class TeacherSalarySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeacherSalary     
        fields = ('url', 'id','amount','year', 'month','teacher')

class IncomeSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Income     
        fields = ('url', 'id','amount','income_type','create_time') 

class TrainingSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Training    
        fields = ('url', 'id','number_of_month','amount','create_time','student') 

class SalaryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherSalary     
        fields = ['id','year', 'month','amount','teacher']

class PaidListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPaid    
        fields = ['id','number_of_course','amount','create_time','student']

class TrainingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training    
        fields = ['id','number_of_month','amount','create_time','student']

class paidPeriodSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    sum_of_paid = serializers.DecimalField(9,2)
    latest_paid_amount = serializers.DecimalField(7,2)
    latest_paid_course = serializers.IntegerField()
    latest_paid_time = serializers.DateField()
    duration = serializers.IntegerField()
    teacher = serializers.CharField()
    
