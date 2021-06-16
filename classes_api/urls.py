from django.urls import path
from .views import ClassesList,CreateClass,EditClass, DeleteClass, CreateTeaching, EditTeaching, DeleteTeaching,\
    CreateStudentSignUp, EditStudentSignUp, DeleteStudentSignUp, TeachingList, StudentsSignUpList

app_name = 'classes_api'

urlpatterns = [
    path('classList/', ClassesList.as_view(), name='classlist'),
    path('createClass/', CreateClass.as_view(), name='classcreate'),
    path('editClass/<int:pk>/', EditClass.as_view(), name='editclass'),
    path('deleteClass/<int:pk>/', DeleteClass.as_view(), name='deleteclass'),
    path('teachingList', TeachingList.as_view(), name='teachinglist'),
    path('createTeaching/', CreateTeaching.as_view(), name='createteaching'),
    path('editTeaching/<int:pk>/', EditTeaching.as_view(), name='editteaching'),
    path('deleteTeaching/<int:pk>/', DeleteTeaching.as_view(), name='deleteteaching'),
    path('SignUpList/', StudentsSignUpList.as_view(), name='signuplist'),
    path('createSignUp/', CreateStudentSignUp.as_view(), name='studentsignup'),
    path('editSignUp/<int:pk>/', EditStudentSignUp.as_view(), name='editsignup'),
    path('deleteSignUp/<int:pk>/', DeleteStudentSignUp.as_view(), name='deletesignup'),
]