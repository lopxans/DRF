from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

import io

# model Object - Single Student Data
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        
        serializer = StudentSerializer(data=python_data) 
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created. '}
            json_res = JSONRenderer().render(res)
            return HttpResponse(json_res, content_type='application/json')
        
        json_res = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_res, content_type='application/json')
