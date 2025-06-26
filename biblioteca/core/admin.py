from django.contrib import admin
from core.models import Livro, Genero, Usuario, Emprestimo

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    """
    Classe de configuração do Admin para o modelo Genero.

    Exibe a lista de gêneros com os campos:
    - id: Identificador do gênero
    - nome: Nome do gênero

    Permite buscar gêneros pelo campo 'nome'.
    """
    list_display = ('id', 'nome')
    search_fields = ('nome',)

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    """
    Classe de configuração do Admin para o modelo Livro.

    Exibe a lista de livros com os campos:
    - id: Identificador do livro
    - titulo: Título do livro
    - autor: Autor do livro
    - isbn: Código ISBN
    - ano_publicacao: Ano de publicação
    - quantidade_disponivel: Quantidade disponível para empréstimo

    Permite filtragem dos livros por:
    - ano_publicacao
    - genero

    Permite busca dos livros pelos campos:
    - titulo
    - autor
    - isbn
    """
    list_display = ('id', 'titulo', 'autor', 'isbn', 'ano_publicacao', 'quantidade_disponivel')
    list_filter = ('ano_publicacao', 'genero')
    search_fields = ('titulo', 'autor', 'isbn')

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    """
    Classe de configuração do Admin para o modelo Usuario.

    Exibe a lista de usuários com os campos:
    - id: Identificador do usuário
    - nome: Nome do usuário
    - email: Email do usuário
    - telefone: Telefone do usuário
    - data_cadastro: Data de cadastro do usuário

    Permite busca dos usuários pelos campos:
    - nome
    - email
    """
    list_display = ('id', 'nome', 'email', 'telefone', 'data_cadastro')
    search_fields = ('nome', 'email')

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    """
    Classe de configuração do Admin para o modelo Emprestimo.

    Exibe a lista de empréstimos com os campos:
    - id: Identificador do empréstimo
    - usuario: Usuário que realizou o empréstimo
    - livro: Livro emprestado
    - data_emprestimo: Data do empréstimo
    - data_devolucao: Data da devolução prevista
    - devolvido: Status de devolução (booleano)

    Permite filtragem dos empréstimos por:
    - devolvido
    - data_emprestimo

    Permite busca dos empréstimos pelos campos relacionados:
    - nome do usuário (usuario__nome)
    - título do livro (livro__titulo)
    """
    list_display = ('id', 'usuario', 'livro', 'data_emprestimo', 'data_devolucao', 'devolvido')
    list_filter = ('devolvido', 'data_emprestimo')
    search_fields = ('usuario__nome', 'livro__titulo')
