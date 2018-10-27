from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from .forms import LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'regstration/signup.html'

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'regstration/login.html'

class Top(generic.TemplateView):
    template_name = 'regstration/top.html'

class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'regstration/top.html'
