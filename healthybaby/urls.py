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
    path('posParto/', views.posParto_view, name='posParto'),
    path('consultas/', views.consultas_view, name='consultas'),
    path('consultaOdonto/', views.consultaOdonto_view, name='consultaOdonto'),
    path('cadastroGestante/', views.cadastroGestante_view, name='cadastroGestante'),
]