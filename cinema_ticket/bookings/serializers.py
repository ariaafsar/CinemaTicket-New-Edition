from .models import Booking
from rest_framework.serializers import ModelSerializer
class TicketSerializer(ModelSerializer):
    class Meta :
        model = Booking 
        fields = ["showtime"]

class TitcketBookingSerializer(ModelSerializer) :
    class Meta :
        model = Booking 
        fields= ["name" , "email" , "seats"]
    
