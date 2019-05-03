from django.shortcuts import render, redirect
from django import views
from .models import Movie

class MovieList(views.View):

    def get(self, request):
        movies = Movie.objects.all()

        context = {
            'movies': movies
        }

        template_name = 'main/list.html'

        return render(request, template_name, context)


class MovieDetail(views.View):

    def get(self, request, id):
        movie = Movie.objects.get(id=id)

        context = {
            'movie': movie
        }

        template_name = "main/detail.html"

        return render(request, template_name, context)

class AddMovie(views.View):

    def get(self, request):

        template_name = "main/form.html"

        return render(request, template_name, {})
    
    def post(self, request):

        titulo = request.POST['titulo']
        director = request.POST['director']
        duracion = request.POST['duracion']
        sinopsis = request.POST['sinopsis']

        movie = Movie.objects.create(
            titulo=titulo,
            director=director,
            duracion=duracion,
            sinopsis=sinopsis
        )

        context = {
            'action': 'create'
        }

        return redirect('/movies')


class EditMovie(views.View):
    def get(self, request, id):

        movie = Movie.objects.get(id=id)

        context = {
            'movie': movie,
            'action': 'edit'
        }

        template_name = "main/form.html"

        return render(request, template_name, context)

    def post(self, request, id):

        movie = Movie.objects.get(id=id)
        print(movie.duracion)

        movie.titulo = request.POST['titulo']
        movie.director = request.POST['director']
        movie.duracion = request.POST['duracion']
        movie.sinopsis = request.POST['sinopsis']

        movie.save()

        return redirect('/movies/', movie.id)

class DeleteMovie(views.View):

    def get(self, request, id):

        movie = Movie.objects.get(id=id)

        movie.delete()

        return redirect('/movies/')

