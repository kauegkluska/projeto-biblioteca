"""
Módulo models.py - Define os modelos de dados para um sistema de biblioteca.

Este módulo contém as definições dos modelos Django para:
- Usuários da biblioteca
- Gêneros literários
- Livros do acervo
- Empréstimos de livros
- Notas fiscais (para possíveis cobranças)

As classes seguem o padrão Model do Django ORM com seus respectivos campos e relacionamentos.
"""

from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    """
    Representa um usuário do sistema de biblioteca.
    
    Atributos:
        nome (CharField): Nome completo do usuário (max 100 caracteres)
        email (EmailField): Endereço de e-mail único do usuário
        telefone (CharField): Número de telefone (opcional)
        data_cadastro (DateTimeField): Data/hora de cadastro (automático na criação)
        
    Métodos:
        __str__: Retorna o nome do usuário para representação string
    """
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Retorna representação string do usuário (seu nome)."""
        return self.nome


class Genero(models.Model):
    """
    Representa um gênero literário para classificação de livros.
    
    Atributos:
        nome (CharField): Nome do gênero (max 50 caracteres, único)
        
    Métodos:
        __str__: Retorna o nome do gênero para representação string
    """
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        """Retorna representação string do gênero (seu nome)."""
        return self.nome


class Livro(models.Model):
    """
    Representa um livro do acervo da biblioteca.
    
    Atributos:
        titulo (CharField): Título do livro (max 200 caracteres)
        autor (CharField): Nome do autor (max 100 caracteres)
        editora (CharField): Nome da editora (opcional)
        ano_publicacao (IntegerField): Ano de publicação
        isbn (CharField): Código ISBN único (max 20 caracteres)
        quantidade_total (PositiveIntegerField): Quantidade total de exemplares (default=1)
        quantidade_disponivel (PositiveIntegerField): Quantidade disponível para empréstimo (default=1)
        genero (ForeignKey): Relacionamento com o gênero do livro (pode ser nulo)
        
    Métodos:
        __str__: Retorna o título do livro para representação string
    """
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100, blank=True)
    ano_publicacao = models.IntegerField()
    isbn = models.CharField(max_length=20, unique=True)
    quantidade_total = models.PositiveIntegerField(default=1)
    quantidade_disponivel = models.PositiveIntegerField(default=1)
    
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """Retorna representação string do livro (seu título)."""
        return self.titulo


class Emprestimo(models.Model):
    """
    Registra um empréstimo de livro para um usuário.
    
    Atributos:
        usuario (ForeignKey): Relacionamento com o usuário que fez o empréstimo
        livro (ForeignKey): Relacionamento com o livro emprestado
        data_emprestimo (DateField): Data do empréstimo (automático na criação)
        data_devolucao (DateField): Data prevista para devolução
        devolvido (BooleanField): Indica se o livro foi devolvido (default=False)
        
    Métodos:
        __str__: Retorna string formatada com info do empréstimo
    """
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField()
    devolvido = models.BooleanField(default=False)

    def __str__(self):
        """Retorna string formatada no padrão: 'Usuário → Livro (Data)'."""
        return f"{self.usuario} → {self.livro} ({self.data_emprestimo})"
    
    
class NotaFiscal(models.Model):
    """
    Representa uma nota fiscal (para possíveis cobranças relacionadas a empréstimos).
    
    Atributos:
        numero (CharField): Número da nota fiscal (único, max 20 caracteres)
        data_emissao (DateField): Data de emissão (default=data atual)
        cliente (CharField): Nome do cliente (max 100 caracteres)
        valorTotal (DecimalField): Valor total da nota (10 dígitos, 2 decimais)
        descricao (TextField): Descrição dos serviços/produtos (opcional)
        
    Métodos:
        __str__: Retorna string formatada com número NF e cliente
    """
    numero = models.CharField(max_length=20, unique=True)
    data_emissao = models.DateField(default=timezone.now)
    cliente = models.CharField(max_length=100)
    valorTotal = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True)
    
    def __str__(self):
        """Retorna string formatada no padrão: 'NF-Número | Cliente: Nome'."""
        return f"NF-{self.numero} | Cliente: {self.cliente}"