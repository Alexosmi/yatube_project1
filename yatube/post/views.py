from django.shortcuts import render


def index(request):
    return render('Заглавная страница')


def group_posts(request, slug):
    return render('Посты по группам')

# Create your views here.
