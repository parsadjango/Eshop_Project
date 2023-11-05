from django.urls import path
from . import views

urlpatterns = [
    path("register", views.RegisterView.as_view(), name="register-page"),
    path("login", views.LoginView.as_view(), name="login-page"),
    path("activate-code/<str:email_active_code>", views.ActivateAccountView.as_view(), name="activate-page"),
]
