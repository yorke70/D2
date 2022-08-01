import django.forms
from django_filters import FilterSet, DateFilter, ModelMultipleChoiceFilter, CharFilter
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

    post_name = CharFilter(label='Заголовок содержит', field_name='post_name', lookup_expr='icontains')
    class Meta:
        model = Post
        fields = ['post_name', 'category', 'time_in']
        # fields = {
        #     'post_name': ['icontains'],
        # }х

