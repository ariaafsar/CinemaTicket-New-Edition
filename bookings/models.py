from django.db import models
from cinemas.models import Showtime

class Booking(models.Model):
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    seats = models.PositiveIntegerField()

    def __str__(self):
        return f"Booking by {self.name} for {self.seats} seats"
