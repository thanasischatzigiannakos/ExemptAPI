from datetime import datetime

from rest_framework import serializers, status
from users.models import User, Professor, Student
from classes.models import SchoolClass, TeachingOfClass, StudentSignUp


class CustomUserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')


class StudentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Student
        fields = ('user',)


class EachClassSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = SchoolClass
        fields = ('name', 'id', 'description')


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


class UserIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',)


class StudentIdSerializer(serializers.ModelSerializer):
    user = UserIdSerializer()

    class Meta:
        model = Student
        fields = ('user',)


class ProfessorIdSerializer(serializers.ModelSerializer):
    user = UserIdSerializer()

    class Meta:
        model = Professor
        fields = ('user',)


class TeachingIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachingOfClass
        fields = ('id',)


class MyTeachingsSerializer(serializers.ModelSerializer):
    professor = EachProfSerializer()
    schoolClass = EachClassSerializer()

    class Meta:
        model = TeachingOfClass
        fields = ('id', 'schoolClass', 'class_year', 'semester', 'professor'
                  , 'theory_weight', 'lab_weight', 'theory_rule', 'lab_rule')


class ClassSignUpSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    teaching = TeachingSerializer()

    class Meta:
        model = StudentSignUp
        fields = ('id', 'teaching', 'student', 'theory_score', 'lab_score'
                  , 'final_score')


class StudentSignUpToClass(serializers.ModelSerializer):
    student = StudentIdSerializer(read_only=True)
    teaching = TeachingIdSerializer(read_only=True)

    class Meta:
        model = StudentSignUp
        fields = ('id', 'teaching', 'student')

    def create(self, validated_data):
        teaching = validated_data.pop('teaching')
        teaching = teaching["id"]
        teaching = TeachingOfClass.objects.get(id=teaching)
        print(teaching)
        student=validated_data.pop('student')
        student = student["user"]
        student = Student.objects.get(user = student)
        sign_up = StudentSignUp(teaching = teaching, student=student)
        sign_up.save()
        print(student)
        return sign_up
