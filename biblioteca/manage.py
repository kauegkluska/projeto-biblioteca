#!/usr/bin/env python
"""Utilitário de linha de comando para tarefas administrativas do Django."""

import os
import sys

# Adiciona o diretório do projeto ao sys.path para garantir a resolução correta dos módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def main():
    """
    Executa as tarefas administrativas do Django.

    Define a variável de ambiente `DJANGO_SETTINGS_MODULE` para o módulo de configurações padrão
    do projeto (neste caso, 'biblioteca.settings') e então tenta executar os comandos de linha
    de comando do Django. Em caso de falha ao importar o Django, uma exceção com mensagem
    explicativa será lançada.
    
    Levanta:
        ImportError: Se o Django não estiver instalado ou disponível no PYTHONPATH.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Não foi possível importar o Django. Você tem certeza de que ele está instalado e "
            "disponível na variável de ambiente PYTHONPATH? Você esqueceu de ativar o ambiente virtual?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # Ponto de entrada do script
    main()
