from django.shortcuts import render

from .models import DoencaCategoria, DoencaGrupo

from django.core.paginator import Paginator

def home(request):
    """Funcão para retonar a pagina inicial"""
    return render(request, 'consulta_cids/home.html', {})


def buscar_cids(request):
    """Buscando CIDs"""
    cids_list = DoencaCategoria.objects.all()

    # Buscando CIDS pela descricao
    search = request.GET.get('search')
    if search:
        buscar_descricao=cids_list.filter(descricao__unaccent__icontains=search)
        context = {'cids': buscar_descricao}
        return render(request, 'consulta_cids/search.html', context)
    
    # Buscando CIDS pela descricao pela categoria
    search2 = request.GET.get('search2')
    if search2:
        buscar_descricao=cids_list.filter(categoria__unaccent__icontains=search2)
        context = {'cids': buscar_descricao}
        return render(request, 'consulta_cids/search.html', context)
    else:
        return render(request,'consulta_cids/search_erro.html')


def lista_cids(request):
    """Listando todas as doencas com seu cid e descricao"""
    cids_list = DoencaCategoria.objects.all()

    # Criando paginação
    p = Paginator(DoencaCategoria.objects.all(), 50)
    page = request.GET.get('page')
    cids_pagination = p.get_page(page)
    num_pages = "a" * cids_pagination.paginator.num_pages

    context = {
        'cids_list': cids_list,
        'cids_pagination': cids_pagination,
        'num_pages': num_pages,
        }

    return render(request, 'consulta_cids/list_cids.html', context)


def lista_grupo(request):
    """Listando todos os grupos com seu cidinicial, cidfinal e descricao"""
    cids_list = DoencaGrupo.objects.all()

    # Criando paginação
    p = Paginator(DoencaGrupo.objects.all(), 50)
    page = request.GET.get('page')
    cids_pagination = p.get_page(page)
    num_pages = "a" * cids_pagination.paginator.num_pages

    context = {
        'cids_list': cids_list,
        'cids_pagination': cids_pagination,
        'num_pages': num_pages,
    }

    return render(request, 'consulta_cids/list_group.html', context)
