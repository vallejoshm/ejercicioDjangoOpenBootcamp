from django.shortcuts import render

from .models import Director, Genre, Movie, MovieInstance

def index(request):
    directors = Director.objects.all()
    movies = Movie.objects.all()
    genres = Genre.objects.all()

    return render(
        request,
        'index.html',
        context={
            'directors': directors,
            'movies': movies,
            'genres': genres,
        }
    )