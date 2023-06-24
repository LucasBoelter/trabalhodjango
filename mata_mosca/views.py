from django.shortcuts import render

# MATA MOSCA.

def view_app(request):
    return render(request, 'mata_mosca/paginas/app.html')

def view_game_over(request):
    return render(request, 'mata_mosca/paginas/game_over.html')

def view_inicio(request):
    return render(request, 'mata_mosca/paginas/index.html')

def view_victory(request):
    return render(request, 'mata_mosca/paginas/victory.html')
