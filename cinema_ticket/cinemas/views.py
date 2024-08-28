from django.http import JsonResponse
from .models import Cinema, Showtime
from movies.models import Movie
from django.shortcuts import get_object_or_404

def showtimes_for_movie(request, movie_id):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, id=movie_id)
        showtimes = Showtime.objects.filter(movie=movie).values('id' , 'movie__title', 'cinema__name', 'start_time', 'available_seats')
        return JsonResponse(list(showtimes), safe=False)
    else:
        return JsonResponse({'error': 'Only GET method is allowed'}, status=405)
