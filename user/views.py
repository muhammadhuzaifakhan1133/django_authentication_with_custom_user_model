from rest_framework import generics
from rest_framework.views import APIView
from .models import UserModel
from .serializers import RegisterAndListUserSerializer
from rest_framework.request import Request
from .serializers import RegisterAndListUserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login

class ListUsersGenericView(generics.ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = RegisterAndListUserSerializer

class RegisterUserGenericView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = RegisterAndListUserSerializer
    def create(self, request: Request, *args, **kwargs):
        serialized_data = RegisterAndListUserSerializer(data=request.data)
        if serialized_data.is_valid():
            user: UserModel = serialized_data.save()
            user.set_password(request.data["password"])
            user.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginUserAPIView(APIView):
    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")
        if email is None or password is None:
            return Response({
                "email": [
                    "email is required"
                ],
                "password": [
                    "password is required"
                ]
            })
        user = UserModel.objects.filter(email=email).first()
        if user is None:
            return Response({"email": "No account exists with that email"})
        is_valid_user = authenticate(email=email, password=password)
        if is_valid_user is None:
            return Response({"password": "wrong password"})
        login(user=user, request=request)
        return Response({
            "message": "user login successfully"
        })

class ChangePasswordAPIView(APIView):
    def patch(self, request: Request, id):
        current_password = request.data.get("current_password")
        new_password = request.data.get("new_password")
        if current_password is None or new_password is None:
            errors = {}
            if current_password is None:
                errors["current_password"] = ["current_password is required"]
            if new_password is None:
                errors["new_password"] = ["new_password is required"]
            return Response(errors)
        user = UserModel.objects.filter(pk=id).first()
        if user is None:
            return Response({"error": "user does not exists with the given id"})
        is_valid_current_password = authenticate(email=user.email, password=current_password)
        if is_valid_current_password is None:
            return Response({
                "error": "wrong current password"
            })
        user.set_password(new_password)
        user.save()
        return Response({
            "message": "password changed successfully"
        })