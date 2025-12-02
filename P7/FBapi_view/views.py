from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# GET Method -------------------------------------------------------------------
# @api_view() # GET method or you can you @api_view(['GET'])
# def hello_world(request):
#     return Response({'msg': 'Hello World'})


# POST Method -------------------------------------------------------------------
# @api_view(['POST'])
# def hello_world(request):
#     if request.method == 'POST':
#         print(request.data)
#         return Response({'msg': 'This is post request'})


# GET & POST Method -------------------------------------------------------------------
@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'GET':
        return Response({'msg': 'This is get request'})
    if request.method == 'POST':
        print(request.data)
        return Response({'msg': 'This is post request', 'data':request.data})
