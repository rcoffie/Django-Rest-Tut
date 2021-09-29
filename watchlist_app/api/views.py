from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework.decorators import api_view 
from watchlist_app.models import * 
from . serializers import *
from rest_framework import status 



class StreamPlatFormList(APIView):
  def get(self, request): 
    platform = StreamPlatForm.objects.all()
    serializer = StreamPlatFormSerializer(platform,many=True)
    return Response(serializer.data)
  
  
  def post(self, request):
    serializer = StreamPlatFormSerializer(data=request.data)
    if serializer.is_valid():
      serializes.save() 
      return Response(serializer.data)
    else:
      return Response(serializer.errors)


class WatchList(APIView):
  def get(self , request):
     movie = MovieList.objects.all()
     serializer = MovieListSerializer(movie, many=True)
     return Response(serializer.data)
   
   
   
  def post(self, request):
    serializer = MovieListSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)
    
    
class WatchListDetailView(APIView):
  def get(self, request, pk):
    try: 
      movie = MovieList.objects.get(pk=pk) 
    except MovieList.DoesNotExist:
      return Response({'error':'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
  
    serializer = MovieListSerializer(movie)
    return Response(serializer.data)

  
  def put(self, request, pk):
    movie = MovieList.objects.get(pk=pk)
    serializer = MovieListSerializer(movie, data= request.data)
    if serializer.is_valid(): 
      serializer.save() 
      return Response(serializer.data)
    else: 
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  
  def delete(self, request, pk):
    movie = MovieList.objects.get(pk=pk)
    movie.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
    
    
   


  
  






""" @api_view(['GET','POST'])
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
      
     """