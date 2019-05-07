from django.shortcuts import render
from django.http import HttpResponse

#Trata do tráfego de urls da aplicação web

def home(request):
    context = {
        #'stocks': stock
    }
    return render(request, 'portal/index.html', context)


def about(request):
    return render(request, 'portal/about.html', {'title': 'About Page'})
# Create your views here.
