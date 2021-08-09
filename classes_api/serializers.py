from datetime import datetime

from rest_framework import serializers, status
from users.models import User, Professor, Student
from classes.models import SchoolClass, TeachingOfClass, StudentSignUp


class CustomUserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class StudentSerializer(serializers.ModelSerializer):
    am = serializers.CharField()

    class Meta:
        model = Student
        fields = ('am',)


class EachClassSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = SchoolClass
        fields = ('name', 'id')


class ClassSerializer(serializers.ModelSerializer):
    requiredClasses = EachClassSerializer(many=True)

    class Meta:
        model = SchoolClass
        fields = ('id', 'name', 'description', 'requiredClasses')


class EachProfSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Professor
        fields = ('user',)


class TeachingSerializer(serializers.ModelSerializer):
    professor = EachProfSerializer()
    schoolClass = EachClassSerializer()

    class Meta:
        model = TeachingOfClass
        fields = ('id', 'schoolClass', 'class_year', 'semester', 'professor'
                  , 'theory_weight', 'lab_weight', 'theory_rule', 'lab_rule')


class ClassSignUpSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    class Meta:
        model = StudentSignUp
        fields = ('id', 'teaching', 'student', 'theory_score', 'lab_score'
                  , 'final_score')
