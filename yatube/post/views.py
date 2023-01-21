from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse('Заглавная страница')


def group_posts(request, slug):
    return HttpResponse('Посты по группам')

# Create your views here.
