from django.urls import path
from .views import IndexView, CadastroView, TabelaView, FuncionarioView, produto
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cadastro', CadastroView.as_view(), name='cadastro'),
    path('tabela', TabelaView.as_view(), name='tabela'),
    path('change-password/', auth_views.PasswordChangeView.as_view()),
    path('accounts/login', auth_views.LoginView.as_view(template_name='login.html')),
    path('funcionario/<int:pk>', produto, name='funcionario'),
]
