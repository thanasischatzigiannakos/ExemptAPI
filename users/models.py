from django.db import models
import datetime
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, user_name, first_name, last_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, last_name, password, **other_fields)

    def create_user(self , email, user_name, first_name, last_name, password, type,  **other_fields ):
        if not email:
            raise ValueError(_('You must provide an email'))
        if not user_name:
            raise ValueError(_('You must provide a username'))
        if not first_name:
            raise ValueError(_('You must provide an first name'))
        if not last_name:
            raise ValueError(_('You must provide a last name'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, first_name=first_name, last_name=last_name, type=type, **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    class Types(models.TextChoices):
        STUDENT = "STUDENT", "Student"
        PROFESSOR = "PROFESSOR", "Professor"

    base_type = Types.STUDENT

    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    type = models.CharField(max_length=20, choices=Types.choices, default=base_type)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name', 'type']

    def __str__(self):
        return self.user_name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    am = models.CharField(max_length=11, unique=True)
    sign_up_date = models.CharField(max_length=4)


class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    class Ranks(models.TextChoices):
        PROFESSOR = "PROFESSOR", "Professor"
        ASSOCIATE_PROFESSOR = "ASSOCIATE_PROFESSOR", "Associate Professor"
        ASSISTANT_PROFESSOR = "ASSISTANT_PROFESSOR", "Assistant Professor"

    base_rank = Ranks.PROFESSOR
    rank = models.CharField(max_length=20, choices=Ranks.choices, default=base_rank)


