import json
import os
from django.shortcuts import render
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Project.models import employee_project, project
from coding_tools.models import codingtools, employee_codingtools
from employee.models import Employee
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import pdfkit
# import pdfkit


@api_view(['POST'])
def index(request):
    if request.method == "POST":
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")

            if username == "admin" and password == "admin123":
                return Response({"status": 200, "verified": True})
            else:
                return Response({"status": 400, "verified": False})
    else:
        return Response({"status": 405, "error": "Method Not Allowed"})


# @api_view(['POST'])
# def add_employee(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         name = data.get('name')
#         summary = data.get('summary')
#         designation = data.get('designation')
#         ctname = data.get('ctname')
#         #adding coding tools
#         # .update(summary="idiot1234")
#         # for obj in data1:
#         # #     print(obj.name)
#         #     obj.delete()
#         if name and summary and designation and ctname:
#             employee1 = Employee(name=name, summary=summary, designation=designation)
#             employee1.save()
#             for obj in ctname:
#                 data1 = codingtools.objects.get(name=obj)
#                 data2 = Employee.objects.get(name=name)
#                 data=employee_codingtools(eid=data2,cid=data1)
#                 data.save()
#             return Response({'message': 'Employee details added successfully'})
#         else:
#             return Response({'error': 'Incomplete data provided'}, status=400)

#     return Response({'error': 'Invalid request method'}, status=405)

@api_view(['POST'])
def add_employee(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        summary = data.get('summary')
        designation = data.get('designation')
        ctname1 = data.get('ctname1', [])  # Assuming the frontend sends two separate lists
        ctname2 = data.get('ctname2', [])

        if name and summary and designation and (ctname1 or ctname2):
            employee1 = Employee(name=name, summary=summary, designation=designation)
            employee1.save()

            for ctname in [ctname1, ctname2]:
                for obj in ctname:
                    try:
                        coding_tool = codingtools.objects.get(name=obj)
                        employee = Employee.objects.get(name=name)
                        employee_coding_tool = employee_codingtools(eid=employee, cid=coding_tool)
                        employee_coding_tool.save()
                    except codingtools.DoesNotExist:
                        return Response({'error': f'Coding tool "{obj}" does not exist'}, status=400)

            return Response({'message': 'Employee details added successfully'})
        else:
            return Response({'error': 'Incomplete data provided'}, status=400)

    return Response({'error': 'Invalid request method'}, status=405)

@api_view(['POST'])
def delete_employee(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        data1 = Employee.objects.filter(name=name)
        data1.delete()
        return Response({'message': 'Employee details deleted successfully'})
    return Response({'error': 'Invalid request method'}, status=405)

@api_view(['POST'])
def update_employee(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        newname=data.get('newname')
        summary = data.get('summary')
        designation = data.get('designation')
        ctname = data.get('ctname')
        if newname:
            data1 = Employee.objects.filter(name=name).update(name=newname, summary=summary, designation=designation)
        else:
            data1 = Employee.objects.filter(name=name).update(summary=summary, designation=designation)
        data2 = Employee.objects.get(name=name)
        data3 = employee_codingtools.objects.filter(eid=data2)
        data3.delete()
        for obj in ctname:
            data1 = codingtools.objects.get(name=obj)
            data2 = Employee.objects.get(name=name)
            data=employee_codingtools(eid=data2,cid=data1)
            data.save()
        if data1:
            return Response({'message': 'Employee details updated successfully'},status=200)
        else:
            return Response({'error': 'Updation failed'}, status=400)

    return Response({'error': 'Invalid request method'}, status=405)

@api_view(['POST'])
def employeelist(request):
    list = []
    if request.method == 'POST':
        data = Employee.objects.all()
        for obj in data:
            clist = []
            tlist = []
            data1=employee_codingtools.objects.filter(eid=obj)
            for obj1 in data1:
                if obj1.cid.type=="coding":
                    clist.append(obj1.cid.name)
                elif obj1.cid.type=="tools":
                    tlist.append(obj1.cid.name)
            list.append({"name":obj.name,"summary":obj.summary,"designation":obj.designation,"tools":tlist,"coding":clist})
        return Response({"data":list},status=200)
    return Response({'error': 'Invalid request method'}, status=405)

# @api_view(['GET'])
# def generate_pdf(request):
#     html = loader.render_to_string('./employee/templates/resume.html', {})
#     pdf = pdfkit.from_string(html)
#     response = HttpResponse(pdf, content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename=my_pdf.pdf'
#     return response

# @api_view(['GET'])
# def generate_pdf(request):
#     data = Employee.objects.all()
#     context = {
#         "employee":data
#     }
#     # html_path = os.path.join(os.path.dirname(__file__), 'templates', 'resume.html')
#     # html = loader.render_to_string(html_path, {})
#     # output_path = 'C:/pythonbackend/resumegenerator/employee/files'
#     # config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
#     # pdf = pdfkit.from_string(html,output_path=output_path,configuration=config)
#     # response = HttpResponse(pdf, content_type='application/pdf')
#     # response['Content-Disposition'] = 'attachment; filename=my_pdf.pdf'
#     # return response
#     return render(request,'resume.html',context)

@api_view(['GET','POST'])
def generate_pdf(request):
    ename = "vasu4"
    data3 = json.loads(request.body)
    ename = data3.get('name')
    list = []
    list1 = []
    data2 = Employee.objects.get(name=ename)
    data = employee_codingtools.objects.filter(eid=data2)
    for obj in data:
        list.append(obj.cid.name)
    data = employee_project.objects.filter(e_id=data2)
    for obj in data:
        list1.append(obj.p_id.name)
    template_path = 'resume.html'
    context = {'name': data2.name,"summary":data2.summary,"designation":data2.designation,'codingtools':list,"projects":list1}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@api_view(['GET'])
def delete_all(request):
    if request.method == 'GET':
        data1 = Employee.objects.all()
        data2 = employee_codingtools.objects.all()
        data3 = codingtools.objects.all()
        data4 = project.objects.all()
        data5 = employee_project.objects.all()
        data1.delete()
        data2.delete()
        data3.delete()
        data4.delete()
        data5.delete()
        return Response({'message': 'All deleted successfully'})
    return Response({'error': 'Invalid request method'}, status=405)
