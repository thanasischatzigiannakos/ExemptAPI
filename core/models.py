from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.type
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    authentication_classes = ()
    serializer_class = MyTokenObtainPairSerializer

