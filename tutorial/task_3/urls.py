from django.urls import path
from . views import StudentView, StudentDetailed

urlpatterns = [
    path('<int:pk>/', StudentDetailed.as_view()),
    path('', StudentView.as_view())
]
