from django.shortcuts import render
from rest_framework.views import APIView
from .models import Student
from .serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status


# Create your views here.
class StudentView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, req):
        query = Student.objects.all()
        serializer = StudentSerializer(query, many=True)

        return Response(serializer.data)

    def post(self, req):
        serializer = StudentSerializer(data=req.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"msg": "student added success", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"msg": "student creation failed", "error": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
