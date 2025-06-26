"""
Módulo urls.py - Define os padrões de URL para o aplicativo da biblioteca.

Este módulo mapeia URLs para views correspondentes, estabelecendo a estrutura de navegação
do sistema. Cada padrão de URL inclui:
- O caminho (path) da URL
- A view associada que processará a requisição
- Um nome único para referência reversa de URLs

Padrões de URL organizados por funcionalidade:
- Página inicial
- Gestão de livros (CRUD)
- Gestão de usuários (CRUD)
- Gestão de empréstimos
- Relatórios
- Gestão de notas fiscais (listagem, criação e geração de PDF)
"""

from django.urls import path
from . import views

urlpatterns = [
    # Página inicial
    path('', views.index, name='index'),
    
    # Operações CRUD para Livros
    path('livros/', views.livros, name='livros'),  # Listagem de todos os livros
    path('livros/create', views.livros_create, name='livro_create'),  # Criação de novo livro
    path('livros/edit/', views.livros_edit, name='livro_edit'),  # Edição de livro existente
    path('livros/delete/', views.livros_delete, name='livro_delete'),  # Exclusão de livro
    
    # Operações CRUD para Usuários
    path('usuarios/', views.usuarios, name='usuarios'),  # Listagem de todos os usuários
    path('usuarios/create', views.usuarios_create, name='usuario_create'),  # Criação de novo usuário
    path('usuarios/edit/', views.usuarios_edit, name='usuario_edit'),  # Edição de usuário existente
    path('usuarios/delete/', views.usuarios_delete, name='usuario_delete'),  # Exclusão de usuário
    
    # Gestão de Empréstimos
    path('emprestimos/create', views.emprestimos_create, name='emprestimos_create'),  # Listagem/gestão de empréstimos
    path('emprestimos/', views.emprestimos, name='emprestimos'),  # Gestão de empréstimos
    
    # Relatórios
    path('relatorios/', views.relatorios, name='relatorios'),  # Página de relatórios

]