
from rest_framework import serializers
from .models import Student
 
class StudentSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student     #指定的模型类
        fields = ('url', 'name', 'level', 'date_of_birth', 'remarks')   #需要序列化的属性