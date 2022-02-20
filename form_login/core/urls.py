from django.urls import path
from .views import LogarView, RegistarView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LogarView.as_view(), name='login'),
    path('login/register/', RegistarView.as_view(), name='register')
]