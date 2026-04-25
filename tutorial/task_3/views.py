from django.shortcuts import render
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.views import View
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializer import EmployeeSerializer
from .models import Employee
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .pagination import PaginationTest
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView


# Create your views here.
# class ApiView(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, req):
#         return self.list(req)

#     def post(self, req):
#         return self.create(req)


# class ApiRetrieve(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, req, pk):
#         return self.retrieve(req)

#     def put(self, req, pk):
#         return self.update(req, pk=pk)

#     def patch(self, req, pk):
#         return self.partial_update(req)
    
#     def delete(self, req, pk):
#         return self.destroy(req)

# class AppView(ReadOnlyModelViewSet):
#     serializer_class = EmployeeSerializer
#     queryset = Employee.objects.all()
    
#     pagination_class = PaginationTest
#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     filterset_fields  = ['age']
#     search_fields = ['name']
#     ordering_fields = ['age']
    
#     def list(self, req):
#         return super().list(req)
    
#     def retrieve(self, req, pk):
#         return super().retrieve(req, pk=pk)
    
#     @action(detail=False, methods=['get', 'post'])
#     def helpme(self, req):
#         return Response({"msg":"it's okay"})

class ApiView(ListCreateAPIView):
    filter_backends=[DjangoFilterBackend, OrderingFilter]
    filterset_fields=['age']
    ordering_fields = ['name']
    
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    
    def list(self, req):
        return super().list(req)
    
    def create(self, req):
        return super().create(req)
    
class ApiViewDetailed(RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    def retrieve(self, req, pk):
        return super().retrieve(req)
    
    def update(self, req, *args, **kwargs):
        return super().update(req, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)