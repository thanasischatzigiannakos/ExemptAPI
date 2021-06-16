from datetime import datetime

from rest_framework import serializers, status
from users.models import User, Professor, Student


class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8,required=False)
    type = serializers.CharField(required=True)
    is_active = serializers.BooleanField(required=False)
    class Meta:
        model = User
        fields = ('email', 'user_name', 'first_name', 'last_name', 'type', 'is_active', 'password')
        # extra_kwargs = {'password': {'write_only':True}}

        def create(self, validated_data):
            password = validated_data.pop('password', None)
            instance = self.Meta.model(**validated_data)
            if password is not None:
                instance.set_password(password)
            instance.save()
            return instance


class StudentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    am = serializers.CharField(required=True)



    class Meta:
        model = Student
        fields = ('user', 'am', 'sign_up_date')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        sign_up = validated_data.pop('sign_up_date')
        user = CustomUserSerializer.create(CustomUserSerializer(), validated_data=user_data)
        student = Student.objects.create(user=user, am=validated_data.pop('am'),
                                                            sign_up_date=sign_up)
        return student


class ProfessorSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(required=True)
    rank = serializers.CharField(required=True)


    class Meta:
        model = Professor
        fields = ('user', 'rank')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUserSerializer.create(CustomUserSerializer(), validated_data=user_data)
        professor = Professor.objects.create(user=user, rank=validated_data.pop('rank'))
        return professor

