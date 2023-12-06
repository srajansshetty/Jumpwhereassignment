from django.db import models

from employee.models import Employee

class codingtools(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default="",unique=True)
    type = models.CharField(max_length=50,default="")
    class Meta:
        db_table='codingtools'

class employee_codingtools(models.Model):
    id = models.AutoField(primary_key=True)
    cid = models.ForeignKey(codingtools,on_delete=models.CASCADE)
    eid = models.ForeignKey(Employee, on_delete=models.CASCADE)
    class Meta:
        db_table='employee_codingtools'
