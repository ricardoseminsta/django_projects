from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView


class LogarView(LoginView):
    template_name = 'login.html'


class RegistarView(TemplateView):
    template_name = 'register.html'


class IndexView(TemplateView):
    template_name = 'index.html'