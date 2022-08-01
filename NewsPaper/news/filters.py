import django.forms
from django_filters import FilterSet, DateFilter, ModelMultipleChoiceFilter
from .models import Post, Category


class NewsFilter(FilterSet):
    time_in = DateFilter(
        lookup_expr='gt',
        widget = django.forms.DateInput(
            attrs={
                'type': 'date'
            }
        ),
        label='Дата создания от:'
    )

    category = ModelMultipleChoiceFilter(
        field_name = 'postcategory__category_name',
        queryset = Category.objects.all(),
        label = 'Категория',
        conjoined = True
    )

    class Meta:
        model = Post
        fields = {
            'post_name': ['icontains'],
        }

