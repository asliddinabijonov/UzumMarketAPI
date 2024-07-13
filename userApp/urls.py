from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [

    path('token/', TokenObtainPairView.as_view()),
    path('token_refresh', TokenRefreshView.as_view()),

]
