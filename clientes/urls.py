from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('cadastro', views.view_clientes, name='view_clientes'),
    path('lista_clientes', views.lista_clientes, name='lista_clientes')
]