from django.contrib.admin import ModelAdmin,register

from movies.models import Movie

@register(Movie)
class MovieAdmin(ModelAdmin):
    pass


