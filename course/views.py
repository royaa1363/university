from rest_framework import viewsets, permissions
from .models import Student, University
from .serializers import StudentSerializer, UniversitySerializer


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    # permission_classes = [permissions.IsAuthenticated]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # permission_classes = [permissions.IsAuthenticated]
