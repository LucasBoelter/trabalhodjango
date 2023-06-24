from django.shortcuts import render

# ORCAMENTO.

def view_inicio(request):
    return render(request, "orcamento/paginas/index.html",)

def view_consulta(request):
    return render(request, "orcamento/paginas/consulta.html",)