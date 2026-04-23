from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from rest_framework import status
from .serializer import StudentSerializer
from django.http import HttpResponse


# Create your views here.
@api_view(["GET", "POST"])
def students(req):
    try:
        if req.method == "GET":
            students = Student.objects.all()
            serialized = StudentSerializer(students, many=True)
            return Response(serialized.data, status=status.HTTP_200_OK)

        if req.method == "POST":
            serialized = StudentSerializer(data=req.data)
            if serialized.is_valid():
                serialized.save()
                return Response(serialized.data, status=status.HTTP_201_CREATED)
            return Response(serialized.errors, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
