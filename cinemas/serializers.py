from rest_framework import serializers
from .models import Cinema , Showtime , CinemaShow

class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'