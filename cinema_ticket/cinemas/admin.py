from django.contrib.admin import ModelAdmin,register

from cinemas.models import Cinema,Showtime


@register(Cinema)
class CinemaAdmin(ModelAdmin):
    pass

@register(Showtime)
class ShowtimeAdmin(ModelAdmin):
    pass


