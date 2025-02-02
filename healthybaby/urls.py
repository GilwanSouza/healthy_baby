from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = "healthybaby"

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('listagem/', views.listagem_view, name='listagem'),
    path('', views.index, name='index'),
    path('logout/', views.user_logout, name='logout'),
]