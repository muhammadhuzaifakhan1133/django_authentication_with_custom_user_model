from .views import ListUsersGenericView, RegisterUserGenericView, LoginUserAPIView, ChangePasswordAPIView
from django.urls import path

urlpatterns = [
    path("users", ListUsersGenericView.as_view()),
    path("register", RegisterUserGenericView.as_view()),
    path("login", LoginUserAPIView.as_view()),
    path("change-password/<id>", ChangePasswordAPIView.as_view()),
]