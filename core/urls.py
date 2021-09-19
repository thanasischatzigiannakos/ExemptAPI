from django.contrib import admin
from django.urls import path, include
from core.models import TokenObtainPairView
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('users.urls', namespace='users')),
    path('api/classes/', include('classes_api.urls', namespace='classes_api')),
    path('', include('classes.urls', namespace='classes_api')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('docs/', include_docs_urls(title='ExemptAPI')),
    path('schema', get_schema_view(
        title="Exempt App",
        description="API for the exempt application",
        version="1.0.0"
    ), name='openapi-schema'),

    # path('api/', include('classes_api.urls', namespace='classes_api')),
]

