import django_tables2 as tables
from .models import Book


class  BookTable(tables.Table):
    class Meta:
        model = Book
    # template_name = 'book_management_app/book_list.html'
     # fields = ['title','file','uploaded_date']
