from rest_framework.serializers import ModelSerializer
from .models import Course, Student


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class StudentSerializer(ModelSerializer):
    course = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = "__all__"
