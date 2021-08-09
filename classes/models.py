from django.db import models
from users.models import Professor, Student


class SchoolClass(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=250)
    requiredClasses = models.ManyToManyField('SchoolCLass', symmetrical=False, blank=True, null=True )

    def __str__(self):
        return self.name


class TeachingOfClass(models.Model):
    schoolClass = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    class_year = models.IntegerField()

    class Semesters(models.TextChoices):
        WI = "WINTER", "Winter"
        SU = "SUMMER", "Summer"

    base_semester = Semesters.SU
    semester = models.CharField(max_length=6, choices=Semesters.choices)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    theory_weight = models.FloatField()
    lab_weight = models.FloatField()
    theory_rule = models.IntegerField(blank=True, null=True)
    lab_rule = models.IntegerField(blank=True, null=True)


class StudentSignUp(models.Model):
    teaching = models.ForeignKey(TeachingOfClass, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student)
    theory_score = models.FloatField(blank=True, null=True)
    lab_score = models.FloatField(blank=True, null=True)
    final_score = models.FloatField(blank=True, null=True)
