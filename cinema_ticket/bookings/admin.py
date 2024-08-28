from django.contrib.admin import ModelAdmin,register
from . models import Booking

@register(Booking)
class BookingAdmin(ModelAdmin):
    pass