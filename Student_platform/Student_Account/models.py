from django.db import models

# Create your models here.

class student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    faculty= models.CharField(max_length=35)
    dept = models.CharField(max_length=25)
    
    class Meta:
        db_table = "students"