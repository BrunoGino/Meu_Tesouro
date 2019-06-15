from django.shortcuts import render
from .models import Title
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import  filters
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
  #  qs = Title.objects.all()
    paginator_qs = filters.TitleFilter(request.GET, queryset=Title.objects.all()).qs
    tipos = Title.objects.values('title_type').distinct()

    # Paginação

    paginator = Paginator(paginator_qs, 15)
    page = request.GET.get('page')
    try:
        titulos = paginator.get_page(page)
    except PageNotAnInteger:
        titulos = paginator.get_page(1)
    except EmptyPage:
        titulos = paginator.get_page(paginator.num_pages)

    # Pega parâmetros do objeto

    title_type = request.GET.get('tipo_titulo')
    title_value_min = request.GET.get('title_value_min')
    title_value_max = request.GET.get('title_value_max')
    ending_date_min = request.GET.get('ending_date_min')
    ending_date_max = request.GET.get('ending_date_max')

    if is_valid_queryparam(title_type) and title_type != 'Tipo do título...':
        paginator_qs = paginator_qs.filter(title_type=title_type)

    if is_valid_queryparam(title_value_min):
        paginator_qs = paginator_qs.filter(title_value__gte=title_value_min)

    if is_valid_queryparam(title_value_max):
        paginator_qs = paginator_qs.filter(title_value__lt=title_value_max)

    if is_valid_queryparam(ending_date_min):
        paginator_qs = paginator_qs.filter(ending_date__gte=ending_date_min)

    if is_valid_queryparam(ending_date_max):
        paginator_qs = paginator_qs.filter(ending_date__lt=ending_date_max)

   # titulos = paginator.paginate_queryset(paginator_qs, request)

# Não filtra, conflito com a paginação

    context = {
       # 'queryset': qs,
        'tipos': tipos,
        'paginator_titulos': titulos,
    }

    return render(request, 'portal/cards.html', context, {'title': 'Títulos'})