from django.shortcuts import render,get_object_or_404, redirect
from django.contrib import messages
from .forms import BookForm
from .models import Book
from .tables import BookTable
from .filters import BookFilter


def home(request):
    return render(request, 'book_management_app/home.html')

def book_form(request):
    if request.method == 'POST':

        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book uploaded successfully!!')
            # return redirect('book-list')
        


    else:
        form = BookForm()
        
    return render(request, 'book_management_app/book_form.html',{'form':form})


def book_list(request):

    book_filter = BookFilter(request.GET, queryset=Book.objects.all())
    books = book_filter.qs


    # q = request.GET.get('q') if request.GET.get('q') !=  None  else ''

    # books = Book.objects.filter(title__icontains = q)
    # print(table)
    table = BookTable(books)
    return render(request, 'book_management_app/book_list.html',{'table':table, 'filter':book_filter})



def book_delete(request, pk):
    if request.method == "POST":
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return redirect('book-list')
    