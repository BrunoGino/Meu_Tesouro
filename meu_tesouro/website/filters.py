import django_filters
from .models import Title


class TitleFilter(django_filters.FilterSet):

    odering = django_filters.ChoiceFilter(label='Ordering',)

    class Meta:
        model = Title
        fields = {'title_type':['icontains'],
                  'title_value':['icontains'],
                  'title_name':['icontains'],
                  'liquidity':['icontains'],
                  'ending_date':['icontains']}
