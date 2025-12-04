from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import io

@csrf_exempt
def student_api(request):
    """ Read and Retrieve Data """
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        
        id = python_data.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    
    """ Create Data """
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created. '}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
            
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    
    """ Update Data """
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        
        # serializer = StudentSerializer(stu, data=python_data)  # Complete Update
        serializer = StudentSerializer(stu, data=python_data, partial=True)  # Partial Update
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Updated. '}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
            
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    
    """ Delete Data """
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg': 'Data Delete. '}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')