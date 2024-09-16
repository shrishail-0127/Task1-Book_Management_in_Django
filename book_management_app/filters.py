import django_filters as filters
from .models import Book


class BookFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    # uploaded_date = filters.DateFilter(field_name='uploaded_date', lookup_expr='exact')

    class Meta:
        model = Book
        fields = ['title']