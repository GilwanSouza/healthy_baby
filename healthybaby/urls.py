from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import listar_gestantes, cadastrar_gestante
from django.conf import settings
from django.conf.urls.static import static

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
    path('cadastroGestante/', views.cadastrar_gestante, name='cadastroGestante'),
    path('gestantes/cadastrar/', cadastrar_gestante, name='cadastrar_gestante'),
    path('gestantes/', listar_gestantes, name='listar_gestantes'),
    
    path('__debug__/', include('debug_toolbar.urls')),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)