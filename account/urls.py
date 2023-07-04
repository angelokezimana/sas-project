from django.urls import path

from . import apis

urlpatterns = [
    path("register/", apis.RegisterApi.as_view(), name="register"),
    path("login/", apis.LoginApi.as_view(), name="Login"),
    path("me/", apis.UserApi.as_view(), name="me"),
    path("logout/", apis.LogoutApi.as_view(), name="logout"),
    path(
        "change-password/",
        apis.ChangePasswordApi.as_view(),
        name="auth_change_password",
    ),
]