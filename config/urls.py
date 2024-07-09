from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static

from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

schema_view = get_schema_view(
    openapi.Info(
        title='UzumMarketAPI',
        default_version='v1',
        description='###',
        terms_of_service='##',
        contact=openapi.Contact(email='###'),
        license=openapi.License(name='###'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', schema_view.with_ui('swagger', cache_timeout=0)),

    path('token/', TokenObtainPairView.as_view()),
    path('token_refresh', TokenRefreshView.as_view()),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
