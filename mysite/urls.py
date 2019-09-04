from django.conf.urls import include,url
from rest_framework import routers
# from api import views
from django.urls import path
from mysite import views

urlpatterns = [
    path('salary/<int:tid>/', views.salaryListByTeacherId),
    path('salary/<int:tid>/<int:y>/', views.salaryListByTeacherIdAndYear),
    path('paid/<int:sid>/', views.paidListByStudentId),
    path('traininglist/<int:sid>/', views.trainingListByStudentId),
    path('paidperiod/', views.paidPeriod),
    path('paidSum/', views.paidSumList),
    path('trainingSum/', views.trainingSumList),
    path('paidlist/', views.StudentPaidList),
    path('traininglist/', views.TrainingList),
    path('paidGroupByStudent/', views.PaidGroudByStudent),
    path('trainingGroupByStudent/', views.TrainingGroudByStudent),
    path('deleteteacher/<int:tid>', views.deleteTeacherForStudent),
]

