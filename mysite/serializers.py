
from rest_framework import serializers
from .models import Student, Teacher, StudentPaid, TeacherSalary, Income, Training
 
class StudentSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student     #model
        fields = ('url', 'name', 'level', 'date_of_birth', 'remarks')   #field

class TeacherSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher     
        fields = ('url', 'name')  

class StudentPaidSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentPaid     
        fields = ('url', 'number_of_course','amount','create_time','student') 

class TeacherSalarySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeacherSalary     
        fields = ('url', 'amount','create_time','teacher')

class IncomeSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Income     
        fields = ('url', 'amount','income_type','create_time') 

class TrainingSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Training    
        fields = ('url', 'number_of_month','amount','create_time','student') 