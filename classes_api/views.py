from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from classes.models import SchoolClass, TeachingOfClass, StudentSignUp
from .serializers import ClassSerializer, TeachingSerializer, ClassSignUpSerializer, StudentSignUpToClass,\
    MyTeachingsSerializer, UpdateTeachingSerializer, MyStudentsGradesSerializer, ClassForGradingSerializer,\
    ClassSignUpUpdateSerializer
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
    serializer_class = UpdateTeachingSerializer


class MyTeachingList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    authentication_classes = ()
    serializer_class = MyTeachingsSerializer

    def get_queryset(self):
        prof = self.kwargs.get('professor_user_id')
        queryset = TeachingOfClass.objects.filter(professor_id=prof)
        return queryset


class DeleteTeaching(generics.RetrieveDestroyAPIView):
    permission_classes = [AllowAny]
    authentication_classes = ()
    queryset = TeachingOfClass.objects.all()
    serializer_class = TeachingSerializer


class StudentsSignUpList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    authentication_classes = ()
    queryset = StudentSignUp.objects.all()
    serializer_class = ClassForGradingSerializer


class CreateStudentSignUp(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request, format='json'):
        serializer = StudentSignUpToClass(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EditStudentSignUp(generics.UpdateAPIView):
    permission_classes = [AllowAny]
    authentication_classes = ()
    queryset = StudentSignUp.objects.all()
    serializer_class = ClassSignUpUpdateSerializer


class DeleteStudentSignUp(generics.RetrieveDestroyAPIView):
    permission_classes = [AllowAny]
    authentication_classes = ()
    queryset = StudentSignUp.objects.all()
    serializer_class = ClassSignUpSerializer


class StudentSignedUpClasses(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    authentication_classes = ()
    serializer_class = ClassSignUpSerializer

    def get_queryset(self):
        student = self.kwargs.get('pk')
        queryset = StudentSignUp.objects.filter(student_id=student)
        return queryset


class StudentsInClass(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    authentication_classes = ()
    serializer_class = ClassSignUpSerializer

    def get_queryset(self):
        teaching = self.kwargs.get('pk')
        queryset = StudentSignUp.objects.filter(teaching_id=teaching)
        return queryset




