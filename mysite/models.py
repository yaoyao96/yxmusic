# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=45)
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=45)
    level = models.IntegerField(default=0)
    date_of_birth = models.DateField(blank=True, null=True)
    remarks = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.name
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.SET_NULL)

class StudentPaid(models.Model):
    number_of_course = models.IntegerField(default=0)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    create_time = models.DateField(auto_now_add=True)
    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.student.name + " / " + self.create_time.strftime('%Y-%m-%d %H:%M:%S') 

class TeacherSalary(models.Model):
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    year = models.IntegerField(default=2019)
    month = models.IntegerField(default=8)
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.teacher.name + " / " + self.create_time.strftime('%Y-%m-%d %H:%M:%S') 

class Income(models.Model):
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    income_type = models.CharField(max_length=45)
    create_time = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.income_type + " / " + self.amount

class Training(models.Model):
    number_of_month = models.IntegerField(default=0)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    create_time = models.DateField(auto_now_add=True)
    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.student.name + " / " + self.create_time.strftime('%Y-%m-%d %H:%M:%S') 

