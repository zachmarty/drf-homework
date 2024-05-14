from datetime import datetime
from django.contrib.auth.hashers import make_password
from rest_framework.generics import CreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from users.models import User
from users.serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        new_user = serializer.save()
        new_user.password = make_password(new_user.password)
        new_user.save()


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        response = super().post(request, *args, **kwargs)
        user = User.objects.get(email=request.data["email"])
        user.last_login = datetime.now()
        user.save()
        return response
