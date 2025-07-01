from django.urls import path
from .views import get_books, add_book,update_book,delete_book # Import the add_book view


urlpatterns = [
      path('books/', get_books, name='get_books'),
      path('add/', add_book, name='add_book'),
      path('update/<int:pk>/', update_book, name='update_book'),
      path('delete/<int:pk>/', delete_book, name='delete_book'),
]