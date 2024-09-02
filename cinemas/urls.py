from django.urls import path
from .views import ShowTimesForMovie

urlpatterns = [
    path('movies/<int:movie_id>/showtimes/',ShowTimesForMovie.as_view() , name='showtimes_for_movie'),
]
