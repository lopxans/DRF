from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import StudentSerializer
from django.http import HttpResponse, JsonResponse
from .models import Student

@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
        """ Read data """
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        # For specific student
        student_id = python_data.get('id')
        if student_id is not None:
            try:
                student = Student.objects.get(id=student_id)
            except Student.DoesNotExist:
                return JsonResponse({'error': 'Student not found'}, status=404)

            serializer = StudentSerializer(student)
            return JsonResponse(serializer.data, safe=False)

        # For all students
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        """ Create data """
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)

        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            response = {'message': 'Data is created. '}
            json_response =  JSONRenderer().render(response)
            return HttpResponse(json_response, content_type='application/json')
        json_response = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_response, content_type='application/json')

    def put(self, request, *args, **kwargs):
        """ Update data """
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        
        id = python_data.get('id')
        student = Student.objects.get(id=id)
        
        serializer = StudentSerializer(student, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {'message': 'Data is Updated. '}
            return JsonResponse(response, safe=False)
        
        response = JSONRenderer().render(serializer.errors)
        return HttpResponse(response, content_type='application/json')
    
    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        
        id = python_data.get('id')
        student_id = Student.objects.get(id=id)
        student_id.delete()
        response = {'message': 'Data Deleted. '}
        return JsonResponse(response, safe=False)