"""
URL configuration for resumegen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import  path
from Project.views import add_project, ass_proj_to_emp, delete_ass_proj_to_emp, delete_project, empproj_list, proj_list, update_project,ass_proj_list
from coding_tools.views import add_codingtools, codingtools_list, countall, delete_codingtools, onlycoding_list, onlytools_list, update_codingtools
from employee.views import add_employee, delete_all, delete_employee, employeelist, generate_pdf, index, update_employee

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', index),
    #emplyee endpoints
    path('api/employee/add',add_employee),
    path('api/pdf',generate_pdf,name='pdfpath'),
    path('api/employee/delete',delete_employee),
    path('api/employee/update',update_employee),
    # path('api-auth/', include('rest_framework.urls'))
    path('api/employee/associate',ass_proj_to_emp),
    path('api/employee/deleteassociate',delete_ass_proj_to_emp),
    path('api/employee/assprjlist',ass_proj_list),
    path('api/employee/employeelist',employeelist),#
    #project endpoints
    path('api/project/add',add_project),
    path('api/project/delete',delete_project),
    path('api/project/update',update_project),
    path('api/project/prjlist',proj_list),
    path('api/project/empproj',empproj_list),
    #Coding tools endpoint
    path('api/codingtools/add',add_codingtools),
    path('api/codingtools/delete',delete_codingtools),
    path('api/codingtools/update',update_codingtools),
    path('api/codingtools/countall',countall),
    path('api/codingtools/list',codingtools_list),#
    path('api/codingtools/toolslist',onlytools_list),#
    path('api/codingtools/codinglist',onlycoding_list),#
    path('api/delete_all',delete_all),
]
