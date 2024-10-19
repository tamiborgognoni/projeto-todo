from django.shortcuts import render

from django.http import HttpResponse

def aluno(request):
    return HttpResponse('Realizado com sucesso a atividade')
