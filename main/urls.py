from django.urls import path
from .views import MovieList, MovieDetail, AddMovie, EditMovie, DeleteMovie

app_name = "main"

urlpatterns = [
    path('', MovieList.as_view()),
    path('<int:id>', MovieDetail.as_view()),
    path('add/', AddMovie.as_view()),
    path('edit/<int:id>', EditMovie.as_view()),
    path('delete/<int:id>', DeleteMovie.as_view())
]