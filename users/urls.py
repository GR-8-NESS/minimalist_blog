from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/',
    auth_views.LoginView.as_view(template_name='registration/login.html'),
    name='login'),
    path('', include('django.contrib.auth.urls'))
]