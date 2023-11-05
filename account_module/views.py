from django.shortcuts import render, redirect, reverse
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from django.views import View
from .models import User
from account_module.forms import RegisterForm, LoginForm

# Create your views here.

user = get_user_model()


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'account_module/Register_component.html',
                      {
                          'Registerform': form
                      })

    def post(self, request):
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'این کاربر قبلا ثبت نام شده است')
            else:
                new_user = User(email=user_email,
                                email_active_code=get_random_string(72),
                                username=user_email,
                                is_active=False,
                                )
                new_user.set_password(user_password)
                new_user.save()
                return redirect(reverse('login-page'))

        return render(request, 'account_module/Register_component.html',
                      {
                          'Registerform': register_form
                      })


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'account_module/Login_component.html',
                      {
                          'loginform': form
                      })

    def post(self, request):
        pass


class ActivateAccountView(View):
    def get(self, request, email_active_code):
        pass

    def post(self, request):
        pass
