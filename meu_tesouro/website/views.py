from django.shortcuts import render
from .models import Title

#Trata do tráfego de urls da aplicação web


def home(request):
    context = {
        #'stocks': stock
    }
    return render(request, 'portal/index.html', {'title': 'Home'}, context)


def about(request):
    return render(request, 'portal/about.html', {'title': 'Sobre'})


def titulos(request):
    all_titles = Title.objects.all()

    context = {'all_titles': all_titles}
    return render(request, 'portal/cards.html', context, {'title': 'Títulos'})
# Create your views here.
