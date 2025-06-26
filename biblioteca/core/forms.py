"""
Formulário para criação e edição de Notas Fiscais.

Este formulário é baseado no modelo NotaFiscal e permite a manipulação dos dados
de notas fiscais através de uma interface web. Utiliza o ModelForm do Django para
gerar automaticamente os campos com base na definição do modelo.

Atributos:
    Meta (classe interna): Configurações específicas do ModelForm
        model (Model): Classe do modelo associado (NotaFiscal)
        fields (list): Lista de campos do modelo que serão incluídos no formulário
            - numero: Número da nota fiscal (deve ser único)
            - data_emissao: Data de emissão da nota
            - cliente: Nome do cliente associado
            - valorTotal: Valor total da nota fiscal
            - descricao: Descrição detalhada (opcional)

Comportamento:
    - Valida automaticamente os campos com base nas regras definidas no modelo
    - Gera widgets apropriados para cada tipo de campo
    - Trata a conversão de dados entre o formulário HTML e o modelo
"""

from django import forms
from .models import NotaFiscal

class NotaFiscalForm(forms.ModelForm):
    """
    Configurações internas do ModelForm para o NotaFiscal.
    
    Define o modelo base e os campos que serão incluídos no formulário gerado.
    """
    class Meta:
        model = NotaFiscal
        fields = ['numero', 'data_emissao', 'cliente', 'valorTotal', 'descricao']