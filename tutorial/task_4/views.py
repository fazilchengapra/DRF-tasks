from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from .models import Course
from .serializer import CourseSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class CourseViewSet(ViewSet):
    def list(self, req):
        query = Course.objects.all()
        serialization = CourseSerializer(query, many=True)

        return Response(serialization.data)

    def retrieve(self, req, pk):
        try:
            query = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response({"err": "Course does not exist"})

        query = Course.objects.get(pk=pk)
        serialization = CourseSerializer(query)

        return Response(serialization.data)

    def update(self, req, pk):
        try:
            query = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response({"err": "Course does not exist"})

        query = Course.objects.get(pk=pk)
        serialization = CourseSerializer(query, data=req.data)

        if serialization.is_valid():
            serialization.save()
            return Response(
                {"res": "Course update success", "data": serialization.data},
                status=status.HTTP_201_CREATED,
            )

        return Response(serialization.data)

    def partial_update(self, req, pk):
        try:
            query = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response({"err": "Course does not exist"})

        query = Course.objects.get(pk=pk)
        serialization = CourseSerializer(query, data=req.data, partial=True)

        if serialization.is_valid():
            serialization.save()
            return Response(
                {"res": "Course patching success", "data": serialization.data},
                status=status.HTTP_201_CREATED,
            )

        return Response(serialization.data)

    def destroy(self, req, pk):
        try:
            query = Course.objects.get(pk=pk)
            query.delete()
            return Response({"res": "Course deleted success"},status=status.HTTP_200_OK)
        except Course.DoesNotExist:
            return Response({"err": "Course does not exist"})
