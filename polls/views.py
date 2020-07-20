from django.http import HttpResponse
from django.shortcuts import render

from .models import *


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # output = ', <br>'.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse(f'Você vendo a pergunta: {question_id}')


def results(request, question_id):
    return HttpResponse(f'Você está vendo os resultados da pergunta: {question_id}')


def vote(request, question_id):
    return HttpResponse(f'Você esta vendo os votos da questão: {question_id}')
