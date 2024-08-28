from django.urls import path
from . import views

urlpatterns = [
    path('movies/<int:movie_id>/showtimes/', views.showtimes_for_movie, name='showtimes_for_movie'),
]
