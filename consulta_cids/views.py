from django.shortcuts import render

from .models import DoencaCategoria

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
