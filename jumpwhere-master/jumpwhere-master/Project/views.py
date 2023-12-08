import json
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Project.models import employee_project, project
from employee.models import Employee
from django.db.models import Q

@api_view(['POST'])
def add_project(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        technology_used = data.get('technology_used')
        description = data.get('description')
        roles = data.get('roles')
        # data1 = project.objects.filter(name="hello1234")
        # .update(summary="idiot1234")
        # for obj in data1:
        # #     print(obj.name)
        #     obj.delete()
        if name and technology_used and description and roles:
            project1 = project(name=name, technology_used=technology_used, description=description,roles=roles)
            project1.save()
            return Response({'message': 'Project details added successfully'},status=200)
        else:
            return Response({'error': 'Incomplete data provided'}, status=400)

    return Response({'error': 'Invalid request method'}, status=405)

@api_view(['POST'])
def delete_project(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        data1 = project.objects.filter(name=name)
        data1.delete()
        return Response({'message': 'project deleted successfully'},status=200)
    return Response({'error': 'Invalid request method'}, status=405)

@api_view(['POST'])
def update_project(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        newname=data.get('newname')
        technology_used = data.get('technology_used')
        description = data.get('description')
        roles = data.get('roles')
        if newname:
            data1 = project.objects.filter(name=name).update(name=newname, technology_used=technology_used, description=description,roles=roles)
        else:
            data1 = project.objects.filter(name=name).update(technology_used=technology_used, description=description,roles=roles)
        if data1:
            return Response({'message': 'project details updated successfully'},status=200)
        else:
            return Response({'error': 'Updation failed'}, status=400)

    return Response({'error': 'Invalid request method'}, status=405)

@api_view(['POST'])
def ass_proj_to_emp(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        ename = data.get('ename')
        pname = data.get('pname')
        # data1 = project.objects.filter(name="hello1234")
        # .update(summary="idiot1234")
        # for obj in data1:
        # #     print(obj.name)
        #     obj.delete()
        if ename and pname:
            # data1 = project.objects.filter(name=pname).first()
            # data2 = Employee.objects.filter(name=ename).first()
            data1 = project.objects.get(name=pname)
            data2 = Employee.objects.get(name=ename)
            data=employee_project(e_id=data2,p_id=data1)
            data.save()
            return Response({'message': 'Project details added successfully'},status=200)
        else:
            return Response({'error': 'Incomplete data provided'}, status=400)

    return Response({'error': 'Invalid request method'}, status=405)

@api_view(['POST'])
def delete_ass_proj_to_emp(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        ename = data.get('ename')
        if ename:
            data2 = Employee.objects.get(name=ename)
            data = employee_project.objects.filter(e_id=data2)
            print(data)
            for obj in data:
                obj.delete()
            return Response({'message': 'Project details deleted successfully'},status=200)
        else:
            return Response({'error': 'Incomplete data provided'}, status=400)

    return Response({'error': 'Invalid request method'}, status=405)

@api_view(['POST'])
def ass_proj_list(request):
    list=[]
    if request.method == 'POST':
        data = json.loads(request.body)
        ename = data.get('ename')
        if ename:
            data2 = Employee.objects.get(name=ename)
            data = employee_project.objects.filter(e_id=data2)
            print(data)
            for obj in data:
                list.append(obj.p_id.name)
            return Response({"projects":list},status=200)
        else:
            return Response({'error': 'Incomplete data provided'}, status=400)

    return Response({'error': 'Invalid request method'}, status=405)

@api_view(['POST'])
def proj_list(request):
    list=[]
    if request.method == 'POST':
            data = project.objects.all()
            print(data)
            for obj in data:
                list.append({'name':obj.name,"technology_used":obj.technology_used,"description":obj.description,"roles":obj.roles})
            return Response({"projects":list},status=200)

    return Response({'error': 'Invalid request method'}, status=405)

@api_view(['POST'])
def empproj_list(request):
    list=[]
    if request.method == 'POST':
            data = Employee.objects.all()
            print(data)
            for obj in data:
                data1 = employee_project.objects.filter(e_id=obj)
                plist=[]
                for obj1 in data1:
                    plist.append(obj1.p_id.name)
                print(plist)
                list.append({'name':obj.name,"mappedproject":plist})
            return Response({"projects":list},status=200)

    return Response({'error': 'Invalid request method'}, status=405)