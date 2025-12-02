from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt

from .models import Student
from .serializers import StudentSerializer

import io

@csrf_exempt
def student_api(request):
    
    # Read Data   ------------------------------------------------
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            student_id = Student.objects.get(id=id)
            serializer = StudentSerializer(student_id)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
        
    # Create Data ------------------------------------------------
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            response = {'Message': 'Data is created. '}
            json_response = JSONRenderer().render(response)
            return HttpResponse(json_response, content_type='application/json')
        
        json_response = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    
    # Update Data ------------------------------------------------
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        
        id = python_data.get('id')
        student_id = Student.objects.get(id=id)
        
        serializer = StudentSerializer(student_id, data=python_data, partial=True) # Partial Update
        # serializer = StopAsyncIteration(student_id, data=python_data)   # Complete Update
        
        if serializer.is_valid():
            serializer.save()
            res = {'Message': 'Data Updated!! '}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    
    
    # Delete Data ------------------------------------------------
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'Message': 'Data Deleted!!'}
        return JsonResponse(res, safe=False)