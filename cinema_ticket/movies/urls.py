from django.urls import path
from .views import MovieSerializer

urlpatterns = [
    path('movies/', MovieSerializer.as_view(), name='movie-list'),
]
