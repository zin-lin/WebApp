from django.urls import path

#from . import views
from .views import HomeView, ArtView


urlpatterns=[

    #path('', views.home, name='home.html'),
    path('', HomeView.as_view(), name='home'),
    path('articleofmine/<int:pk>',ArtView.as_view(), name="article-detail" )

    ]
