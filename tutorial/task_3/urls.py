from django.urls import path, include
from .views import ApiView, ApiViewDetailed
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('employee/', ApiView.as_view()),
    path('employee/<int:pk>/', ApiViewDetailed.as_view())
]
