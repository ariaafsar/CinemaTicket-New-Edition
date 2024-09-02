from .models import Booking
from rest_framework.serializers import ModelSerializer , ValidationError
from cinemas.models import Showtime
from django.shortcuts import get_object_or_404

class TicketSerializer(ModelSerializer):
    class Meta :
        model = Booking 
        fields = ["showtime"]

class TitcketBookingSerializer(ModelSerializer) :
    class Meta :
        model = Booking 
        fields= ["name" , "email" , "seats"]
    
class BookingSerializer(ModelSerializer) :
    class Meta :
        model = Booking
        fields = ['id', 'showtime_id', 'name', 'email', 'seats']

    def valdate(self , data):
        showtime = get_object_or_404(Showtime, id=data["showtime"].id)
        if data["seats"] > data["showtime"].available_seats:
            raise ValidationError("Not enough available seats")
        return data
    
    def create(self , validated_data):
        showtime = validated_data.pop("showtime")
        booking = Booking.objects.create(showtime=showtime , **validated_data)
        showtime.available_seats -= booking.seats
        showtime.save()
        return booking