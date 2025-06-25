from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('livros/', views.livros, name='livros'),
    path('livros/create', views.livros_create, name='livro_create'),
    path('livros/edit/', views.livros_edit, name='livro_edit'),
    path('livros/delete/', views.livros_delete, name='livro_delete'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('usuarios/create', views.usuarios_create, name='usuario_create'),
    path('usuarios/edit/', views.usuarios_edit, name='usuario_edit'),
    path('usuarios/delete/', views.usuarios_delete, name='usuario_delete'),
    path('emprestimos/', views.emprestimos, name='emprestimos'),
    path('relatorios/', views.relatorios, name='relatorios'),
]
