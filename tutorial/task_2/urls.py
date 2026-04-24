from django.urls import path
from .views import Task_View

urlpatterns = [
    path("", Task_View.as_view()),
    path("/<int:id>", Task_View.as_view())
]
