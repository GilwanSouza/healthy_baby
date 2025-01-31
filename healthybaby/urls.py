from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = "healthybaby"

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='usuarios/login'), name='logout'),
    path('', views.index, name='index'),
    path('register/', auth_views.LogoutView.as_view(next_page='listagem'), name='listagem'),
]