from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import *

from .permissions import *
from .serializers import *


class UserRegisterAPIView(APIView):
    @swagger_auto_schema(
        request_body=UserRegisterSerializer
    )
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(role='Regular')
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UserDetailsAPIView(APIView):
    permission_classes = [IsRegularUser]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class UserUpdateAPIView(APIView):
    permission_classes = [IsRegularUser]

    @swagger_auto_schema(
        request_body=UserUpdateSerializer
    )
    def put(self, request):
        serializer = UserUpdateSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class UserDeleteAPIView(APIView):
    permission_classes = [IsRegularUser]

    def delete(self, request):
        user = request.user
        user.delete()
        return Response(status=204)
