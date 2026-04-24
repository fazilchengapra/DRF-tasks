from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from .serializer import StudentSerializer
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from django.http import JsonResponse


# Create your views here.
class Task_View(APIView):
    def get(self, req):
        students = Student.objects.all()
        serialized = StudentSerializer(students, many=True)
        return Response(serialized.data)

    def post(self, req):
        serialized = StudentSerializer(data=req.data)

        if serialized.is_valid():
            serialized.save()
            return Response(
                {"res": "data added success", "data": serialized.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(serialized.errors)

    def put(self, req, id):
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({"res": "User does not exist!"})
        serialized = StudentSerializer(student, data=req.data)
        if serialized.is_valid():
            serialized.save()
            return Response({"res": "Data updated success!", "data": serialized.data})
        return Response(serialized.errors)
    
    def delete(self, req, id):
        try:
            student = Student.objects.all()
        except Student.DoesNotExist:
            return Response({
                'msg':"Something went wrong"
            })
        student.delete()
        return Response({'msg':'student deleted success!'})
