from django.db import models

class Person(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    class Meta:
        db_table='user'


class Employee(models.Model):
    id = models.IntegerField(auto_created=True,primary_key=True)
    name = models.CharField(max_length=40,default="",unique=True)
    summary =models.CharField(max_length=100,default="")
    designation = models.CharField(max_length=40,default="")
    class Meta:
        db_table='employee'







