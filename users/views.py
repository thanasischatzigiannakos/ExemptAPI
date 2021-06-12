import logging

from rest_framework.generics import UpdateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer, StudentSerializer, ProfessorSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAdminUser
from users.models import Student, User, Professor

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG)

class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserPostDetail(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

class StudentPostDetail(RetrieveAPIView):
    permission_classes = [AllowAny]
    lookup_field = "user_id"
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



class ProfessorPostDetail(RetrieveAPIView):
    permission_classes = [AllowAny]
    lookup_field = "user_id"
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class StudentCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, format='json'):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


class ProfessorCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = ProfessorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ActivateAccounts(UpdateAPIView):
     permission_classes = [AllowAny]
     queryset = User.objects.all()
     serializer_class = CustomUserSerializer








#REGISTRATION COMPLETE MUST START WORK ON FUNCTIONALITY

""" Concrete View Classes
    #CreateAPIView
    Used for create-only endpoints.
    #ListAPIView
    Used for read-only endpoints to represent a collection of model instances.
    #RetrieveAPIView
    Used for read-only endpoints to represent a single model instance.
    #DestroyAPIView
    Used for delete-only endpoints for a single model instance.
    #UpdateAPIView
    Used for update-only endpoints for a single model instance.
    ##ListCreateAPIView
    Used for read-write endpoints to represent a collection of model instances.
    RetrieveUpdateAPIView
    Used for read or update endpoints to represent a single model instance.
    #RetrieveDestroyAPIView
    Used for read or delete endpoints to represent a single model instance.
    #RetrieveUpdateDestroyAPIView
    Used for read-write-delete endpoints to represent a single model instance.
    """