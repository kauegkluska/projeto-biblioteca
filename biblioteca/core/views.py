
from django.shortcuts import render, get_object_or_404
from core.models import Livro, Usuario, Emprestimo

def index(request):
    return render(request, 'core/index.html')

def livros(request):
    livros = Livro.objects.all()
    return render(request, 'core/livro/livros.html', {'livros': livros })

def livros_create(request):
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
    usuarios = Usuario.objects.all()
    return render(request, 'core/usuario/usuarios.html', {'usuarios': usuarios})

def usuarios_create(request):
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



def emprestimos(request):
    livros = Livro.objects.all()
    usuarios = Usuario.objects.all()
    context = {
        'livros': livros,
        'usuarios': usuarios,
    }

    if request.method == 'POST':
        livro_id = request.POST.get('livro_id')
        usuario_id = request.POST.get('usuario_id')
        data_devolucao = request.POST.get('data_devolucao')

        livro = get_object_or_404(Livro, pk=livro_id)
        usuario = get_object_or_404(Usuario, pk=usuario_id)

        if livro.quantidade_disponivel > 0:
            livro.quantidade_disponivel -= 1
            livro.save()
            Emprestimo.objects.create(
                livro=livro,
                usuario=usuario,
                data_devolucao=data_devolucao
            )
            context.update({
                'success': 'Empréstimo realizado com sucesso!',
                'livro': livro,
                'usuario': usuario,
                'livro_selecionado_id': livro.id,
                'usuario_selecionado_id': usuario.id,
            })
        else:
            context['error'] = 'Livro indisponível para empréstimo.'

    return render(request, 'core/emprestimo/emprestimos.html', context)
    

def relatorios(request):
    return render(request, 'core/relatorios.html')
