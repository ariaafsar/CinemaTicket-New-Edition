from django.urls import path
from . import views

urlpatterns = [
    path('showtimes/<int:showtime_id>/book/', views.book_ticket, name='book_ticket'),
    path('welcome/' , views.welcome, name='welcome'),
    path('bookings/', views.list_bookings, name='list_bookings'),
]
