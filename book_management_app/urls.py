from django.urls import path
from .import views

urlpatterns = [

    path('book-form/',views.book_form, name='book-form'),
    path('book-list/',views.book_list, name='book-list'),

]