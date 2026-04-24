from django.urls import path
from .views import students, fn_view, MyView

urlpatterns = [
    path('students', students ),
    path('api', fn_view),
    path('cls', MyView.as_view())
]
