from django.contrib import admin

# Register your models here.
from .models import Student, Teacher, StudentPaid, TeacherSalary, Income, Training

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(TeacherSalary)
admin.site.register(StudentPaid)
admin.site.register(Income)
admin.site.register(Training)