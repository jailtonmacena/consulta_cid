from django.shortcuts import render

def home(request):
    """Funcão para retonar a pagina inicial"""
    return render(request, 'consulta_cids/home.html', {})

