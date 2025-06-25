# admin.py
from django.contrib import admin
from core.models import Livro, Genero, Usuario, Emprestimo

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'isbn', 'ano_publicacao', 'quantidade_disponivel')
    list_filter = ('ano_publicacao', 'genero')  # <- CORRIGIDO
    search_fields = ('titulo', 'autor', 'isbn')

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'data_cadastro')
    search_fields = ('nome', 'email')

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'livro', 'data_emprestimo', 'data_devolucao', 'devolvido')
    list_filter = ('devolvido', 'data_emprestimo')
    search_fields = ('usuario__nome', 'livro__titulo')
