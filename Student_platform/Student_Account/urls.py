from django.urls import path
from Student_Account import views

urlpatterns = [
path('', views.index, name='index'),
path('student', views.student, name='student'),

]