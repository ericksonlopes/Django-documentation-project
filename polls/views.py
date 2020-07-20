from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    return HttpResponse(f'Você vendo a pergunta: {question_id}')


def results(request, question_id):
    return HttpResponse(f'Você está vendo os resultados da pergunta: {question_id}')


def vote(request, question_id):
    return HttpResponse(f'Você esta vendo os votos da questão: {question_id}')