from django.shortcuts import render
from django.contrib import messages
from .forms import BookForm
from .models import Book
from .tables import BookTable


def book_form(request):
    if request.method == 'POST':

        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'Book uploaded successfully!!')
        else:
            messages.error(request, 'Please enter valid details')


    else:
        form = BookForm()
        
    return render(request, 'book_management_app/book_form.html',{'form':form})


def book_list(request):
    books = Book.objects.all()
    # print(table)
    table = BookTable(books)
    return render(request, 'book_management_app/book_list.html',{'table':table})
