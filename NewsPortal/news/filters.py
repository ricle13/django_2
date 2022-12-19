from django_filters import FilterSet, CharFilter, DateFilter, ChoiceFilter
from django.forms import DateInput
from .models import Category

class NewsFilter(FilterSet):
    FILTER_CHOICES = []
    chois = Category.objects.all().values('pk', 'category_name')
    for choi in chois:
        FILTER_CHOICES.append((choi['pk'], choi['category_name']))
    name = CharFilter(field_name = 'header', label='Название')
    category = ChoiceFilter(choices = FILTER_CHOICES)
    start_date = DateFilter(field_name='post_time',
                                           widget= DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                                           lookup_expr='gt', label='Статьи начиная с')

