from django.urls import path
from catalogacao.views import admin_home
from catalogacao import views

app_name = 'catalogacao'

urlpatterns = [
    # Mapeia a URL raiz ('/') para a função lista_documentos na views.py
    path('', views.dashboard, name='dashboard'),
    path('admin-area/', views.admin_home, name='admin_home'),

]