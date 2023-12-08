from django.db import models

from employee.models import Employee

class project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default="",unique=True)
    technology_used = models.CharField(max_length=50,default="")
    description = models.CharField(max_length=200,default="")
    roles = models.CharField(max_length=50,default="")
    class Meta:
        db_table='project'

class employee_project(models.Model):
    id = models.AutoField(primary_key=True)
    p_id = models.ForeignKey(project,on_delete=models.CASCADE,related_name='pid',default=None)
    e_id = models.ForeignKey(Employee, on_delete=models.CASCADE,related_name='eid',default=None)
    class Meta:
        db_table='employee_project'
