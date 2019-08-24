from django.conf.urls import include,url
from rest_framework import routers
# from api import views
from django.urls import path
from mysite import views

urlpatterns = [
    path('salary/<int:tid>/', views.salaryListByTeacherId),
    path('salary/<int:tid>/<int:y>/', views.salaryListByTeacherIdAndYear),
    path('paid/<int:sid>/', views.paidListByStudentId),
    path('training/<int:sid>/', views.trainingListByStudentId),
]

