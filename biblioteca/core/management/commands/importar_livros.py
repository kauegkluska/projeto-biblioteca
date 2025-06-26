import csv
from django.core.management.base import BaseCommand
from core.models import Livro  # ajuste para seu app e modelo corretos

class Command(BaseCommand):
    help = 'Importa livros de um arquivo CSV'

    def add_arguments(self, parser):
        parser.add_argument('arquivo_csv', type=str, help='Caminho para o arquivo CSV')

    def handle(self, *args, **kwargs):
        caminho = kwargs['arquivo_csv']
        with open(caminho, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            count = 0
            for row in reader:
                Livro.objects.create(
                    titulo=row['titulo'],
                    autor=row['autor'],
                    editora=row['editora'],
                    ano_publicacao=row['ano_publicacao'],
                    isbn=row['isbn'],
                    quantidade_total=row['quantidade_total'],
                    quantidade_disponivel=row['quantidade_disponivel'],
                    genero_id=row['genero_id']
                )
                count += 1
        self.stdout.write(self.style.SUCCESS(f'{count} livros importados com sucesso!'))