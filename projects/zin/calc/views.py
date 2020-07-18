from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

#Import Templates to see views in actual page not admin area

from django.views.generic import ListView, DetailView

from .models import Post


'''def home(request):
    #return HttpResponse("Hello World")

    return render(request, "home.html", {})
    return HttpResponse('Hello World')
    '''

class HomeView(ListView):
    model = Post
    template_name= "home.html"

class ArtView(DetailView):
    model= Post
    template_name= "article.html"
