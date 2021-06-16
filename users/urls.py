from django.urls import path
from .views import CustomUserCreate, BlacklistTokenUpdateView, StudentCreate, ProfessorCreate , ActivateAccounts,\
    UserPostDetail, StudentPostDetail, ProfessorPostDetail
from django.contrib import admin

app_name = 'users'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('createUser/', CustomUserCreate.as_view(), name="create_user"),
    path('userInfo/<int:pk>/', UserPostDetail.as_view(), name="user_info"),
    path('createStudent/', StudentCreate.as_view(), name="create_student"),
    path('studentInfo/<int:user_id>/', StudentPostDetail.as_view(), name="user_info"),
    path('createProfessor/', ProfessorCreate.as_view(), name="create_professor"),
    path('professorInfo/<int:user_id>/', ProfessorPostDetail.as_view(), name="user_info"),
    path('activateUser/<int:pk>/', ActivateAccounts.as_view(), name="activate_account"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist')
]