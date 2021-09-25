from rest_framework.response import Response 
from rest_framework.decorators import api_view 
from watchlist_app.models import * 
from . serializers import *
from rest_framework import status 



@api_view(['GET','POST'])
def Movie_List(request):
  if request.method == 'GET':
    movies = Movie.objects.all() 
    serializer = MovieSerializer(movies, many=True)
    return Response (serializer.data)
  
  if request.method == 'POST':
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response (serializer.data)
    else:
      return Response(serializer.errors)
    



@api_view(['GET', 'PUT', 'DELETE'])
def Movie_Detail(request, pk):
  if request.method == 'GET':
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response (serializer.data)
  
  if request.method == 'PUT':
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie, data=request.data)
    if serializer.is_valid():
      serializer.save() 
      return Response(serializer.data)
    else:
      return Response (serializer.errors)
    
    
  if request.method == 'DELETE':
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    content = {'please movie ': 'deleted'}
    return Response(content, status=status.HTTP_404_NOT_FOUND)
      
    