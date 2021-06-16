from datetime import datetime

from rest_framework import serializers, status
from users.models import User, Professor, Student
from classes.models import SchoolClass, TeachingOfClass, StudentSignUp

class EachClassSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = SchoolClass
        fields = ('name',)



class ClassSerializer(serializers.ModelSerializer):
    requiredClasses = EachClassSerializer(many=True)

    class Meta:
        model = SchoolClass
        fields = ('id', 'name', 'description', 'requiredClasses')


class TeachingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachingOfClass
        fields = ('id', 'schoolCLass', 'class_year', 'semester', 'professor'
                  , 'theory_weight', 'lab_weight', 'theory_rule', 'lab_rule')


class ClassSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSignUp
        fields = ('id', 'teaching', 'student', 'theory_score', 'lab_score'
                  , 'final_score')
