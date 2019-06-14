from django.shortcuts import render
from .models import Title
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Trata do tráfego de urls da aplicação web


def is_valid_queryparam(param):
    return param != '' and param is not None


def home(request):
    return render(request, 'portal/index.html', {'title': 'Home'})


def about(request):
    return render(request, 'portal/about.html', {'title': 'Informações'})


def contato(request):
    return render(request, 'portal/contato.html', {'title': 'Contato'})


@login_required()
def title(request):
    # Querysets
    qs = Title.objects.all()
    tipos = Title.objects.values('title_type').distinct()

    # Paginação

    paginator = Paginator(qs, 15)
    page = request.GET.get('page')
    try:
        titulos = paginator.page(page)
    except PageNotAnInteger:
        titulos = paginator.page(1)
    except EmptyPage:
        titulos = paginator.page(paginator.num_pages)

    # Pega parâmetros do objeto

    title_type = request.GET.get('tipo_titulo')
    title_value_min = request.GET.get('title_value_min')
    title_value_max = request.GET.get('title_value_max')
    ending_date_min = request.GET.get('ending_date_min')
    ending_date_max = request.GET.get('ending_date_max')

    if is_valid_queryparam(title_type) and title_type != 'Tipo do título...':
        qs = qs.filter(title_type=title_type)

    if is_valid_queryparam(title_value_min):
        qs = qs.filter(title_value__gte=title_value_min)

    if is_valid_queryparam(title_value_max):
        qs = qs.filter(title_value__lt=title_value_max)

    if is_valid_queryparam(ending_date_min):
        qs = qs.filter(ending_date__gte=ending_date_min)

    if is_valid_queryparam(ending_date_max):
        qs = qs.filter(ending_date__lt=ending_date_max)

    context = {
        'queryset': qs,
        'tipos': tipos,
        'paginator_titulos': titulos,
    }

    return render(request, 'portal/cards.html', context, {'title': 'Títulos'})