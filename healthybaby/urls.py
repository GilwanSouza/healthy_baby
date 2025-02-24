from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import listar_gestantes, cadastrar_gestante, salvar_dentes
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "healthybaby"

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('', views.index, name='index'),
    path('logout/', views.user_logout, name='logout'),
    path('consultas/', views.consultas_view, name='consultas'),
    path('consultaOdonto/', views.consultaOdontoCadastro, name='consultaOdonto'),
    path('cadastroGestante/', views.cadastrar_gestante, name='cadastroGestante'),
    path('listagem/', views.listar_gestantes, name='listagem'),
    path('posParto/', views.posParto_cadastro, name='posParto'),
    path("salvar-dentes/", views.salvar_dentes, name="salvar_dentes"),
    ]