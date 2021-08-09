from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from classes.models import SchoolClass, TeachingOfClass, StudentSignUp
from .serializers import ClassSerializer, TeachingSerializer, ClassSignUpSerializer
from rest_framework.permissions import AllowAny, IsAdminUser


class ClassesList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    authentication_classes = ()
    queryset = SchoolClass.objects.all()
    serializer_class = ClassSerializer


class CreateClass(generics.CreateAPIView):
    permission_classes = [AllowAny]
    authentication_classes = ()
    queryset = SchoolClass.objects.all()
    serializer_class = ClassSerializer


class EditClass(generics.UpdateAPIView):
    permission_classes = [AllowAny]
    authentication_classes = ()
    queryset = SchoolClass.objects.all()
    serializer_class = ClassSerializer


class DeleteClass(generics.RetrieveDestroyAPIView):
    permission_classes = [AllowAny]
    authentication_classes = ()
    queryset = SchoolClass.objects.all()
    serializer_class = ClassSerializer


class TeachingList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    authentication_classes = ()
    queryset = TeachingOfClass.objects.all()
    serializer_class = TeachingSerializer


class CreateTeaching(generics.CreateAPIView):
    permission_classes = [AllowAny]
    authentication_classes = ()
    queryset = TeachingOfClass.objects.all()
    serializer_class = TeachingSerializer


class EditTeaching(generics.UpdateAPIView):
    permission_classes = [AllowAny]
    authentication_classes = ()
    queryset = TeachingOfClass.objects.all()
    serializer_class = TeachingSerializer


class DeleteTeaching(generics.RetrieveDestroyAPIView):
    permission_classes = [AllowAny]
    authentication_classes = ()
    queryset = TeachingOfClass.objects.all()
    serializer_class = TeachingSerializer


class StudentsSignUpList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    authentication_classes = ()
    queryset = StudentSignUp.objects.all()
    serializer_class = ClassSignUpSerializer


class CreateStudentSignUp(generics.CreateAPIView):
    permission_classes = [AllowAny]
    authentication_classes = ()
    queryset = StudentSignUp.objects.all()
    serializer_class = ClassSignUpSerializer


class EditStudentSignUp(generics.UpdateAPIView):
    permission_classes = [AllowAny]
    authentication_classes = ()
    queryset = StudentSignUp.objects.all()
    serializer_class = ClassSignUpSerializer


class DeleteStudentSignUp(generics.RetrieveDestroyAPIView):
    permission_classes = [AllowAny]
    authentication_classes = ()
    queryset = StudentSignUp.objects.all()
    serializer_class = ClassSignUpSerializer
