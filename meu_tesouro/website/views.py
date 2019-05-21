from django.shortcuts import render
from .models import Title
from django.contrib.auth.decorators import login_required

# Trata do tráfego de urls da aplicação web


def home(request):
    return render(request, 'portal/index.html', {'title': 'Home'})


def about(request):
    return render(request, 'portal/about.html', {'title': 'Sobre'})

@login_required
def titulos(request):
    all_titles = Title.objects.all()[:20]

    context = {'all_titles': all_titles}
    return render(request, 'portal/cards.html', context, {'title': 'Títulos'})

