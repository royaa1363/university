from rest_framework import serializers
from .models import Student, Teacher, Major, Session, Main_unit, Public_unit, Term


class Main_unitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main_unit
        fields = ['name']


class Public_unitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Public_unit
        fields = ['name']


class MajorSerializer(serializers.ModelSerializer):
    main_units = Main_unitSerializer()
    public_units = Public_unitSerializer()

    class Meta:
        model = Major
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    major = MajorSerializer()

    class Meta:
        model = Student
        fields = '__all__'


class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = '__all__'


class SessionSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    term = TermSerializer()

    class Meta:
        model = Session
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    unit = Main_unitSerializer()

    class Meta:
        model = Teacher
        fields = '__all__'


class CustomTeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ['last_name']
