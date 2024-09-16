import django_tables2 as tables
from .models import Book


class  BookTable(tables.Table):

    actions = tables.TemplateColumn(
        template_code='<button><a href=" {{ record.file.url }}">View</a></button> <form method="POST" action = "{% url \'book-delete\' record.id %}" style="display:inline-block;"> {% csrf_token %} <button type="submit"> Delete </button> </form>',
        verbose_name = 'Actions'
    )

   
   

    class Meta:
        model = Book
    # template_name = 'book_management_app/book_list.html'
     # fields = ['title','file','uploaded_date']
