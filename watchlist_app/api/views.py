from rest_framework.response import Response 
from rest_framework.decorators import api_view 
from watchlist_app.models import * 
from . serializers import *



@api_view(['GET'])
def Movie_List(request):
  movies = Movie.objects.all() 
  serializer = MovieSerializer(movies, many=True)
  return Response (serializer.data)



@api_view()
def Movie_Detail(request, pk):
  movie = Movie.objects.get(pk=pk)
  serializer = MovieSerializer(movie)
  return Response (serializer.data)