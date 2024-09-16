from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name='home'),
    path('book-form/',views.book_form, name='book-form'),
    path('book-list/',views.book_list, name='book-list'),
    path('book-delete/<int:pk>/',views.book_delete, name="book-delete"),

]