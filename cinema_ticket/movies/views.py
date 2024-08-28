from django.http import JsonResponse
from .models import Movie

def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all().values('id', 'title', 'description', 'duration_minutes', 'release_date')
        return JsonResponse(list(movies), safe=False)
    else:
        return JsonResponse({'error': 'Only GET method is allowed'}, status=405)
