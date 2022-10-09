import uuid

from django.db import models
from django.urls import reverse


class Director(models.Model):
    first_name = models.CharField(max_length=100, help_text="Nombre_director/a")
    last_name = models.CharField(max_length=100, help_text="Apellido_director/a")
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_dead = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('director-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)



class Genre(models.Model):
    name = models.CharField(max_length=64, help_text="Nombre del género")

    def __str__(self):
        return self.name



class Movie(models.Model):
    title = models.CharField(max_length=100, help_text="Título de la película")
    premiere = models.DateField(null=True, blank=True)
    genre = models.ManyToManyField(Genre)
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)

    def getTitle(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie-detail', args=[str(self.id)])


class MovieInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para esta película")
    movie = models.ForeignKey('Movie', on_delete=models.SET_NULL, null=True)

    LOAN_STATUS = (
        ('ob', 'on billboard'),
        ('os', 'on streaming'),
        ('oc', 'on cable tv'),
    )

    status = models.CharField(max_length=2, choices=LOAN_STATUS, blank=True, default='ob', help_text="Disponiblilidad de la película")
