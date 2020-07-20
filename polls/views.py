from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import *


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # output = ', <br>'.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls.html', {'question': question})

    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('A Pergunta não existe')
    # return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    return HttpResponse(f'Você está vendo os resultados da pergunta: {question_id}')


def vote(request, question_id):
    return HttpResponse(f'Você esta vendo os votos da questão: {question_id}')
