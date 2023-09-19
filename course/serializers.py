from rest_framework import serializers
from .models import Student, University


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['name']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'university', 'id']


