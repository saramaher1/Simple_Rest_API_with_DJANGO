from http.client import responses
from typing_extensions import Required
from urllib import request
from django.http import JsonResponse
import rest_framework
from .models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

@api_view(['GET','POST'])
def student_list(request):


  if request.method =='GET':
      students = Student.objects.all()
      serializer = StudentSerializer(students, many=True)
      return JsonResponse({'students':serializer.data})

  if request.method =='POST':
    serializer= StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
@api_view(['GET','PUT','DELETE'])       
def student_detail(request,id):
  try:
    student=Student.objects.get(pk=id)
  except Student.DoNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method =='GET'  :
    serializer=StudentSerializer(student) 
    return Response(serializer.data) 

  if request.method =='PUT'  :
    serializer=StudentSerializer(student,data=request.data) 
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)  


