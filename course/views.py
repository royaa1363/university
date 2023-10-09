from rest_framework import viewsets
from .models import Student, Teacher, Major, Session, Main_unit, Public_unit, Term
from .serializers import StudentSerializer, TeacherSerializer, MajorSerializer, SessionSerializer, \
    Main_unitSerializer, Public_unitSerializer, TermSerializer


class MajorViewSet(viewsets.ModelViewSet):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer


class TermViewSet(viewsets.ModelViewSet):
    queryset = Term.objects.all()
    serializer_class = TermSerializer


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class Main_unitViewSet(viewsets.ModelViewSet):
    queryset = Main_unit.objects.all()
    serializer_class = Main_unitSerializer


class Public_unitViewSet(viewsets.ModelViewSet):
    queryset = Public_unit.objects.all()
    serializer_class = Public_unitSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
