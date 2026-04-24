from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    is_adult = serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields = '__all__'
        
    # def validate_age(self, value):
    #     if value < 18:
    #         raise serializers.ValidationError('Age must be a 18 years old')
    #     return value
        
    def get_is_adult(self, obj):
        return obj.age >= 18
    
    def validate(self, data):
        if data['name'] == 'admin' and data['age'] < 18:
            raise serializers.ValidationError("admin must be older than 18 years old")
        return data