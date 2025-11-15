from django.shortcuts import render
from catalogacao.models import Tipo, Genero, Documento
from django.contrib.auth.decorators import login_required  # Opcional: para garantir que apenas admins logados acessem


# Defina a função da view. Ela deve receber um objeto request como argumento.
@login_required  # Garante que o usuário esteja logado (se necessário)
def admin_home(request):
    # Lógica de backend pode ser adicionada aqui (ex: buscar dados do banco de dados)
    # Exemplo de dados para passar para o template:
    context = {
        'username': request.user.username,
        'page_title': 'Página Inicial do Admin'
    }
    return render(request, 'catalogacao/admin_home.html', context)

def dashboard(request):
    """
    View principal que exibe o catálogo de documentos.
    Recupera todos os documentos e os passa para o template.
    """
    # Recupera todos os documentos, ordenados por data de cadastro (mais recente primeiro)
    documentos = Documento.objects.select_related('genero__tipo').all()

    context = {
        'documentos': documentos,
        'titulo_pagina': 'Catálogo de Documentos Textuais'
    }
    return render(request, 'catalogacao/dashboard.html', context)


