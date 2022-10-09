from django.contrib import admin

from .models import Director, Movie, MovieInstance, Genre

admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(MovieInstance)
admin.site.register(Genre)
