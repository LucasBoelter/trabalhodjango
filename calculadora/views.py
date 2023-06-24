from django.shortcuts import render

# CALCULADORA.

def view_inicio(request):
    return render(request, 'calculadora/paginas/index.html')