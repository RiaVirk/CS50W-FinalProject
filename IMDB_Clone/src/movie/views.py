from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Movie


class MovieList(ListView):
    model = ModelName
    # template_name = ""


class movieDetail(DetailView):
    model = Movie
