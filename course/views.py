from pprint import pprint

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Student, Teacher, Major, Session, Main_unit, Public_unit, Term
from .serializers import StudentSerializer, TeacherSerializer, MajorSerializer, SessionSerializer, \
    Main_unitSerializer, Public_unitSerializer, TermSerializer, CustomTeacherSerializer


class MajorViewSet(viewsets.ModelViewSet):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer


class TermViewSet(viewsets.ModelViewSet):
    queryset = Term.objects.all()
    serializer_class = TermSerializer


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.filter(major_id=1)
    # queryset = Session.objects.all()
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

    def get_queryset(self):
        if self.action == 'list':
            return Teacher.objects.all()
        else:
            return Teacher.objects.get(id=1)

    def get_serializer_class(self):
        if self.action != 'list':
            return CustomTeacherSerializer
        else:
            return TeacherSerializer


class TeacherApiView(APIView):

    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers)
        return Response(serializer.data)

@api_view(["GET"])
def teacher_apiview(request):
    # teachers = Teacher.objects.all()
    # serializer = TeacherSerializer(teachers)
    # return Response(serializer.data)

    return Response(TeacherSerializer(Teacher.objects.all(), many=True).data)
