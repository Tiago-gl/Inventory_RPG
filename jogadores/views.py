from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Classe, Raca, Personagem  # Certifique-se de ter esses modelos

def jogadores(request):
    if request.method == "GET":
        # Pega todas as classes e raças do banco de dados para exibir no formulário
        classes = Classe.objects.all()
        racas = Raca.objects.all()
        return render(request, 'jogadores.html', {'classes': classes, 'racas': racas})
    
    elif request.method == "POST":
        # Recebe os dados do formulário
        nome = request.POST.get('nome')
        classe_id = request.POST.get('classe')
        raca_id = request.POST.get('raça')
        
        # Recupera as instâncias de Classe e Raca selecionadas
        classe = Classe.objects.get(id=classe_id)
        raca = Raca.objects.get(id=raca_id)
        
        # Cria e salva o novo personagem
        personagem = Personagem(nome=nome, classe=classe, raca=raca)
        personagem.save()
        
        return HttpResponse('Personagem criado com sucesso!')
