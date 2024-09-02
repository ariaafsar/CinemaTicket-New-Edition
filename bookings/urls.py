from django.urls import path
from .views import ListBookings , welcome , BookTicets
urlpatterns = [
    path('showtimes/<int:showtime_id>/book/', BookTicets.as_view(), name='book_ticket'),
    path('welcome/' , welcome, name='welcome'),
    path('bookings/', ListBookings.as_view() , name='list_bookings'),
]
