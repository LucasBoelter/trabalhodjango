from django.shortcuts import render

# HOME.

def view_inicio(request):
    return render(request, 'home/paginas/home.html')
