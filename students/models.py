from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    password = models.CharField(max_length=10)

class Meta:
    db_table = "student"

