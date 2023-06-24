from django.shortcuts import render

# UBER.

def view_contato(request):
    return render(request, "uber/paginas/contato.html")

def view_inicio(request):
    return render(request, "uber/paginas/index.html")

def view_login(request):
    return render(request, "uber/paginas/login.html")

def view_mobile(request):
    return render(request, "uber/paginas/mobile.html")

def view_register_motorista(request):
    return render(request, "uber/paginas/register_motorista.html")

def view_register(request):
    return render(request, "uber/paginas/register.html")

def view_servicos(request):
    return render(request, "uber/paginas/servicos.html")

def view_sobre(request):
    return render(request, "uber/paginas/sobre.html")

def view_uber_eats(request):
    return render(request, "uber/paginas/uber_eats.html")