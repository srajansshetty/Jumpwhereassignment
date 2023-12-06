import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Project.models import project

from coding_tools.models import codingtools, employee_codingtools
from employee.models import Employee
from django.db.models import Q

@api_view(['POST'])
def add_codingtools(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        type = data.get('type')
        # .update(summary="idiot1234")
        # for obj in data1:
        # #     print(obj.name)
        #     obj.delete()
        if name and type:
            codetools1 = codingtools(name=name,type=type)
            codetools1.save()
            return Response({'message': 'skills added successfully'},status=200)
        else:
            return Response({'error': 'Incomplete data provided'}, status=400)

    return Response({'error': 'Invalid request method'}, status=405)

@api_view(['POST'])
def delete_codingtools(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        data1 = codingtools.objects.filter(name=name)
        data1.delete()
        return Response({'message': 'skill details deleted successfully'},status=200)
    return Response({'error': 'Invalid request method'}, status=405)

@api_view(['POST'])
def update_codingtools(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        newname=data.get('newname')
        type = data.get('type')
        if newname:
            data1 = codingtools.objects.filter(name=name).update(name=newname,type=type)
        else:
            data1 = codingtools.objects.filter(name=name).update(type=type)
        if data1:
            return Response({'message': 'skill details updated successfully'},status=200)
        else:
            return Response({'error': 'Updation failed'}, status=400)

    return Response({'error': 'Invalid request method'}, status=405)

@api_view(['POST'])
def onlycoding_list(request):
    list=[]
    if request.method == 'POST':
            type = 'coding'
            data = codingtools.objects.filter(type=type)
            print(data)
            for obj in data:
                list.append({'name':obj.name})
            return Response({"projects":list},status=200)

    return Response({'error': 'Invalid request method'}, status=405)

@api_view(['POST'])
def onlytools_list(request):
    list=[]
    if request.method == 'POST':
            type =  'tools'
            data = codingtools.objects.filter(type=type)
            print(data)
            for obj in data:
                list.append({'name':obj.name})
            return Response({"projects":list},status=200)

    return Response({'error': 'Invalid request method'}, status=405)

@api_view(['POST'])
def codingtools_list(request):
    list=[]
    if request.method == 'POST':
            data = codingtools.objects.all()
            print(data)
            for obj in data:
                list.append({'name':obj.name})
            return Response({"projects":list},status=200)

    return Response({'error': 'Invalid request method'}, status=405)

@api_view(['POST'])
def countall(request):
    if request.method == 'POST':
            ccount = codingtools.objects.filter(type="coding").count()
            tcount = codingtools.objects.filter(type="tools").count()
            pcount = project.objects.count()
            ecount = Employee.objects.count()
            return Response({"codingcount":ccount,"toolscount":tcount,"projectscount":pcount,"employeecount":ecount},status=200)

    return Response({'error': 'Invalid request method'}, status=405)

@api_view(['POST'])
def ass_ct_to_emp(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        ename = data.get('ename')
        ctname = data.get('ctname')
        # data1 = project.objects.filter(name="hello1234")
        # .update(summary="idiot1234")
        # for obj in data1:
        # #     print(obj.name)
        #     obj.delete()
        if ename and ctname:
            # data1 = project.objects.filter(name=pname).first()
            # data2 = Employee.objects.filter(name=ename).first()
            data1 = codingtools.objects.get(name=ctname)
            data2 = Employee.objects.get(name=ename)
            data=employee_codingtools(eid=data2,cid=data1)
            data.save()
            return Response({'message': 'Project details added successfully'},status=200)
        else:
            return Response({'error': 'Incomplete data provided'}, status=400)

    return Response({'error': 'Invalid request method'}, status=405)

@api_view(['POST'])
def delete_ct_to_emp(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        ename = data.get('ename')
        ctname = data.get('ctname')
        if ename and ctname:
            data1 = codingtools.objects.get(name=ctname)
            data2 = Employee.objects.get(name=ename)
            data = employee_codingtools.objects.filter(Q(eid=data2) & Q(cid=data1))
            print(data)
            data.delete()
            return Response({'message': 'Project details deleted successfully'},status=200)
        else:
            return Response({'error': 'Incomplete data provided'}, status=400)

    return Response({'error': 'Invalid request method'}, status=405)

@api_view(['POST'])
def ass_ct_list(request):
    list=[]
    if request.method == 'POST':
        data = json.loads(request.body)
        ename = data.get('ename')
        if ename:
            data2 = Employee.objects.get(name=ename)
            data = employee_codingtools.objects.filter(c_id=data2)
            print(data)
            for obj in data:
                list.append(obj.cid.name)
            print(list)
            return Response({"data":list},status=200)
        else:
            return Response({'error': 'Incomplete data provided'}, status=400)

    return Response({'error': 'Invalid request method'}, status=405)




