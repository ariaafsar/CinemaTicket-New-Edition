from django.http import JsonResponse
from .models import Cinema, Showtime
from movies.models import Movie
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView , RetrieveDestroyAPIView , ListAPIView
from .serializers import Cinema

def showtimes_for_movie(request, movie_id):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, id=movie_id)
        showtimes = Showtime.objects.filter(movie=movie).values('id' , 'movie__title', 'cinema__name', 'start_time', 'available_seats')
        return JsonResponse(list(showtimes), safe=False)
    else:
        return JsonResponse({'error': 'Only GET method is allowed'}, status=405)

class ShowTimesForMovie(ListAPIView) :
    serializer_class = Cinema
    def get_queryset(self) :
        movie_id = self.kwargs['movie_id']
        return Showtime.objects.filter(movie_id=movie_id)
    