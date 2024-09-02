from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from cinemas.models import Showtime
from .models import Booking
import json
import requests
from rest_framework.generics import ListAPIView , RetrieveAPIView , CreateAPIView , DestroyAPIView
from .serializers import TicketSerializer , TitcketBookingSerializer , BookingSerializer

class BookTicets(CreateAPIView) :
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

@csrf_exempt
def book_ticket(request, showtime_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            showtime = get_object_or_404(Showtime, id=showtime_id)

            if data['seats'] > showtime.available_seats:
                return JsonResponse({'error': 'Not enough available seats'}, status=400)

            # Create a new booking
            booking = Booking.objects.create(
                showtime=showtime,
                name=data['name'],
                email=data['email'],
                seats=data['seats']
            )

            # Decrease available seats
            showtime.available_seats -= data['seats']
            showtime.save()

            return JsonResponse({'message': 'Booking successful', 'booking_id': booking.id})
        except (KeyError, json.JSONDecodeError) as e:
            return JsonResponse({'error': 'Invalid data'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)

def list_bookings(request):
    if request.method == 'GET':
        bookings = Booking.objects.select_related('showtime__movie', 'showtime__cinema').all()
        bookings_list = []
        for booking in bookings:
            bookings_list.append({
                'id': booking.id,
                'name': booking.name,
                'email': booking.email,
                'seats': booking.seats,
                'movie_title': booking.showtime.movie.title,
                'cinema_name': booking.showtime.cinema.name,
                'showtime_start': booking.showtime.start_time.strftime('%Y-%m-%d %H:%M:%S'),
            })
        return JsonResponse(bookings_list, safe=False)
    else:
        return JsonResponse({'error': 'Only GET method is allowed'}, status=405)
class ListBookings(ListAPIView) :
    queryset = Booking.objects.all()
    serializerclass = BookingSerializer


def welcome(request):
    return HttpResponse("Welcome to the booking system!")