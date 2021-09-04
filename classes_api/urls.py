from django.urls import path
from .views import ClassesList,CreateClass,EditClass, DeleteClass, CreateTeaching, EditTeaching, DeleteTeaching,\
    CreateStudentSignUp, EditStudentSignUp, DeleteStudentSignUp, TeachingList, StudentsSignUpList, StudentSignedUpClasses,\
    StudentsInClass, MyTeachingList

app_name = 'classes_api'

urlpatterns = [
    path('classList/', ClassesList.as_view(), name='class_list'),
    path('createClass/', CreateClass.as_view(), name='class_create'),
    path('editClass/<int:pk>/', EditClass.as_view(), name='edit_class'),
    path('deleteClass/<int:pk>/', DeleteClass.as_view(), name='delete_class'),
    path('teachingList/', TeachingList.as_view(), name='teaching_list'),
    path('myTeaching/<int:professor_user_id>/', MyTeachingList.as_view(), name='my_teaching'),
    path('createTeaching/', CreateTeaching.as_view(), name='create_teaching'),
    path('editTeaching/<int:pk>/', EditTeaching.as_view(), name='edit_teaching'),
    path('deleteTeaching/<int:pk>/', DeleteTeaching.as_view(), name='delete_teaching'),
    path('SignUpList/', StudentsSignUpList.as_view(), name='signup_list'),
    path('SignedUp/<int:pk>/', StudentSignedUpClasses.as_view(), name='signed_up_list' ),
    path('SignedStudents/<int:pk>/', StudentsInClass.as_view(), name='signedIn' ),
    path('createSignUp/', CreateStudentSignUp.as_view(), name='student_signup'),
    path('editSignUp/<int:pk>/', EditStudentSignUp.as_view(), name='edit_signup'),
    path('deleteSignUp/<int:pk>/', DeleteStudentSignUp.as_view(), name='delete_signup'),
]
