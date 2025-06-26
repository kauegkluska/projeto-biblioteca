"""
Módulo views.py - Contém todas as views do aplicativo core.

Este módulo implementa a lógica de controle para:
- Páginas principais e index
- CRUD de Livros
- CRUD de Usuários
- Gestão de Empréstimos
- Geração de Relatórios
- Gestão de Notas Fiscais (incluindo geração de PDF)

Todas as views seguem o padrão Django de receber um objeto request e retornar
um objeto HttpResponse. As views utilizam templates HTML para renderização.
"""

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.shortcuts import get_object_or_404
from django.shortcuts import render, get_object_or_404, redirect
from core.models import Livro, Usuario, Emprestimo
from core.models import NotaFiscal
from core.forms import NotaFiscalForm
from django.utils import timezone
from django.db.models import Count
from django.db.models.functions import TruncMonth

from django.shortcuts import render, get_object_or_404
from django.db.models import Q
def index(request):
    """
    View para a página inicial do sistema.
    
    Args:
        request: Objeto HttpRequest contendo os dados da requisição
    
    Returns:
        HttpResponse: Renderiza o template core/index.html
    """
    return render(request, 'core/index.html')

def livros(request):
    """
    Lista todos os livros com opção de busca.
    
    Realiza uma busca nos livros caso um parâmetro 'q' seja fornecido,
    pesquisando em título, autor ou ISBN. Os resultados são ordenados por título.
    
    Args:
        request: Objeto HttpRequest que pode conter:
            - q: Parâmetro opcional de busca
    
    Returns:
        HttpResponse: Renderiza core/livro/livros.html com contexto:
            - livros: QuerySet de livros (filtrados ou todos)
    """
    query = request.GET.get('q', '').strip()
    
    if query:
        livros = Livro.objects.filter(Q(titulo__icontains=query) | Q(autor__icontains=query) | Q(isbn__icontains=query))
    else:
        livros = Livro.objects.all()
    livros = livros.order_by('titulo')
    return render(request, 'core/livro/livros.html', {'livros': livros })

def livros_create(request):
    """
    View para criação de novos livros.
    
    Trata tanto a exibição do formulário (GET) quanto o processamento
    dos dados submetidos (POST). Em caso de sucesso, retorna com flag 'success'.
    
    Args:
        request: Objeto HttpRequest que pode conter dados POST com:
            - titulo, autor, editora, ano_publicacao, isbn, quantidade_total, quantidade_disponivel
    
    Returns:
        HttpResponse: Renderiza core/livro/livros_create.html com contexto:
            - success: Flag indicando criação bem-sucedida (opcional)
    """
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        editora = request.POST.get('editora')
        ano_publicacao = request.POST.get('ano_publicacao')
        isbn = request.POST.get('isbn')
        quantidade_total = request.POST.get('quantidade_total')
        quantidade_disponivel = request.POST.get('quantidade_disponivel')

        livro = Livro(
            titulo=titulo,
            autor=autor,
            editora=editora,
            ano_publicacao=ano_publicacao,
            isbn=isbn,
            quantidade_total=quantidade_total,
            quantidade_disponivel=quantidade_disponivel
        )
        livro.save()

        return render(request, 'core/livro/livros_create.html', {'success': True})
    
    return render(request, 'core/livro/livros_create.html')
    
def livros_edit(request):
    """
    View para edição de livros existentes.
    
    Exibe lista de livros para seleção e formulário de edição.
    Em caso de sucesso, retorna com flag 'success' e dados do livro editado.
    
    Args:
        request: Objeto HttpRequest que pode conter POST com:
            - livro_id: ID do livro a editar
            - campos do livro para atualização
    
    Returns:
        HttpResponse: Renderiza core/livro/livros_edit.html com contexto:
            - livros: QuerySet de todos os livros
            - livro: Objeto livro sendo editado (após POST)
            - success: Flag de sucesso (opcional)
    """
    livros = Livro.objects.all()
    if request.method == 'POST':
        livro_id = request.POST.get('livro_id')
        livro = get_object_or_404(Livro, pk=livro_id)

        livro.titulo = request.POST.get('titulo')
        livro.autor = request.POST.get('autor')
        livro.editora = request.POST.get('editora')
        livro.ano_publicacao = request.POST.get('ano_publicacao')
        livro.isbn = request.POST.get('isbn')
        livro.quantidade_total = request.POST.get('quantidade_total')
        livro.quantidade_disponivel = request.POST.get('quantidade_disponivel')
        livro.save()

        return render(request, 'core/livro/livros_edit.html', {
            'livros': livros,
            'livro': livro,
            'success': True
        })

    return render(request, 'core/livro/livros_edit.html', {
        'livros': livros
    })
    
def livros_delete(request):
    """
    View para exclusão de livros.
    
    Exibe lista de livros para seleção e processa a exclusão via POST.
    Após exclusão, atualiza a lista e retorna com flag 'success'.
    
    Args:
        request: Objeto HttpRequest que pode conter POST com:
            - livro_id: ID do livro a excluir
    
    Returns:
        HttpResponse: Renderiza core/livro/livros_delete.html com contexto:
            - livros: QuerySet de livros atualizado
            - success: Flag de sucesso (opcional)
    """
    livros = Livro.objects.all()

    if request.method == 'POST':
        livro_id = request.POST.get('livro_id')
        livro = get_object_or_404(Livro, pk=livro_id)
        livro.delete()
        return render(request, 'core/livro/livros_delete.html', {
            'success': True,
            'livros': Livro.objects.all()
        })

    return render(request, 'core/livro/livros_delete.html', {'livros': livros})

def usuarios(request):
    """
    Lista todos os usuários cadastrados.
    
    Returns:
        HttpResponse: Renderiza core/usuario/usuarios.html com contexto:
            - usuarios: QuerySet de todos os usuários
    """
    usuarios = Usuario.objects.all()
    return render(request, 'core/usuario/usuarios.html', {'usuarios': usuarios})

def usuarios_create(request):
    """
    View para criação de novos usuários.
    
    Valida se o nome foi fornecido (campo obrigatório).
    Em caso de sucesso, retorna com flag 'success'.
    
    Args:
        request: Objeto HttpRequest que pode conter POST com:
            - nome (obrigatório), email, telefone
    
    Returns:
        HttpResponse: Renderiza core/usuario/usuarios_create.html com contexto:
            - success: Flag de sucesso (opcional)
            - error: Mensagem de erro se nome não fornecido (opcional)
    """
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        email = request.POST.get('email', '').strip()
        telefone = request.POST.get('telefone', '').strip()

        if not nome:
            return render(request, 'core/usuario/usuarios_create.html', {
                'error': 'O campo nome é obrigatório.'
            })

        usuario = Usuario(
            nome=nome,
            email=email,
            telefone=telefone
        )
        usuario.save()

        return render(request, 'core/usuario/usuarios_create.html', {'success': True})

    return render(request, 'core/usuario/usuarios_create.html')

def usuarios_edit(request):
    """
    View para edição de usuários existentes.
    
    Similar à livros_edit, mas para usuários.
    
    Args:
        request: Objeto HttpRequest que pode conter POST com:
            - usuario_id: ID do usuário a editar
            - campos do usuário para atualização
    
    Returns:
        HttpResponse: Renderiza core/usuario/usuarios_edit.html com contexto:
            - usuarios: QuerySet de todos os usuários
            - usuario: Objeto usuário sendo editado (após POST)
            - success: Flag de sucesso (opcional)
    """
    usuarios = Usuario.objects.all()
    if request.method == 'POST':
        usuario_id = request.POST.get('usuario_id')
        usuario = get_object_or_404(Usuario, pk=usuario_id)

        usuario.nome = request.POST.get('nome')
        usuario.email = request.POST.get('email')
        usuario.telefone = request.POST.get('telefone')
        usuario.save()

        return render(request, 'core/usuario/usuarios_edit.html', {
            'usuarios': usuarios,
            'usuario': usuario,
            'success': True
        })

    return render(request, 'core/usuario/usuarios_edit.html', {
        'usuarios': usuarios
    })

def usuarios_delete(request):
    """
    View para exclusão de usuários.
    
    Similar à livros_delete, mas para usuários.
    
    Args:
        request: Objeto HttpRequest que pode conter POST com:
            - usuario_id: ID do usuário a excluir
    
    Returns:
        HttpResponse: Renderiza core/usuario/usuarios_delete.html com contexto:
            - usuarios: QuerySet de usuários atualizado
            - success: Flag de sucesso (opcional)
    """
    usuarios = Usuario.objects.all()

    if request.method == 'POST':
        usuario_id = request.POST.get('usuario_id')
        usuario = get_object_or_404(Usuario, pk=usuario_id)
        usuario.delete()
        return render(request, 'core/usuario/usuarios_delete.html', {
            'success': True,
            'usuarios': Usuario.objects.all()
        })

    return render(request, 'core/usuario/usuarios_delete.html', {'usuarios': usuarios})

def emprestimos_create(request):
    livros = Livro.objects.filter(quantidade_disponivel__gt=0)  
    usuarios = Usuario.objects.all()

    livro_selecionado = None
    usuario_selecionado = None
    success = None
    error = None

    if request.method == 'POST':
        livro_id = request.POST.get('livro_id')
        usuario_id = request.POST.get('usuario_id')
        data_devolucao = request.POST.get('data_devolucao')

        if not livro_id or not usuario_id or not data_devolucao:
            error = "Por favor, preencha todos os campos."
        else:
            try:
                livro_selecionado = Livro.objects.get(id=livro_id)
                usuario_selecionado = Usuario.objects.get(id=usuario_id)

                if livro_selecionado.quantidade_disponivel <= 0:
                    error = "Livro indisponível para empréstimo."
                else:
                    emprestimo = Emprestimo.objects.create(
                        livro=livro_selecionado,
                        usuario=usuario_selecionado,
                        data_emprestimo=timezone.now(),
                        data_devolucao=data_devolucao
                    )
                    livro_selecionado.quantidade_disponivel -= 1
                    livro_selecionado.save()

                    return redirect('emprestimos')  # Redireciona para a lista de empréstimos

            except Livro.DoesNotExist:
                error = "Livro não encontrado."
            except Usuario.DoesNotExist:
                error = "Usuário não encontrado."
            except Exception as e:
                error = f"Ocorreu um erro: {str(e)}"
    

    context = {
        'livros': livros,
        'usuarios': usuarios,
        'livro': livro_selecionado,
        'usuario': usuario_selecionado,
        'success': success,
        'error': error,
    }
    return render(request, 'core/emprestimo/emprestimos_create.html', context)




def emprestimos(request):
    emprestimos = Emprestimo.objects.all()
    query = request.GET.get('q', '')

    if query:
        emprestimos = emprestimos.filter(
            Q(usuario__nome__icontains=query) | 
            Q(livro__titulo__icontains=query) |
            Q(data_emprestimo__icontains=query)
        )
        
    emprestimos = emprestimos.order_by('-data_emprestimo')
    
    context = {
        'emprestimos': emprestimos,
        'query': query,
    }

    if request.method == 'POST':
        emprestimo_id = request.POST.get('emprestimo_id')
        emprestimo = get_object_or_404(Emprestimo, pk=emprestimo_id)
        
        if 'devolver' in request.POST:
            emprestimo.devolvido = True
            emprestimo.livro.quantidade_disponivel += 1
            emprestimo.livro.save()
            emprestimo.save()
            context['success'] = "Empréstimo devolvido com sucesso!"
        
        elif 'excluir' in request.POST:
            emprestimo.delete()
            context['success'] = "Empréstimo excluído com sucesso!"

        emprestimos = Emprestimo.objects.all()
        if query:
            emprestimos = emprestimos.filter(
                Q(usuario__nome__icontains=query) | 
                Q(livro__titulo__icontains=query) |
                Q(data_emprestimo__icontains=query)
            )
        emprestimos = emprestimos.order_by('-data_emprestimo')
        context['emprestimos'] = emprestimos

    return render(request, 'core/emprestimo/emprestimos.html', context)

  

def relatorios(request):
    dados = (
        Emprestimo.objects
        .annotate(mes=TruncMonth('data_emprestimo'))
        .values('mes')
        .annotate(total=Count('id'))
        .order_by('mes')
    )

    labels = [d['mes'].strftime('%b/%Y') for d in dados]
    valores = [d['total'] for d in dados]

    context = {
        'labels': labels,
        'valores': valores,
    }
    return render(request, 'core/relatorios.html', context)
