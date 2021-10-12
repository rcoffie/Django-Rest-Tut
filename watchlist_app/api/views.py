from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework.decorators import api_view 
from watchlist_app.models import * 
from . serializers import *
from rest_framework import status 
from rest_framework import mixins, generics 
from rest_framework.exceptions import ValidationError





class ReviewList(generics.ListCreateAPIView):
  queryset = Review.objects.all() 
  serializer_class = ReviewSerializer 


class ReviewList(generics.ListAPIView): 
  serializer_class = ReviewSerializer 
  
  def get_queryset(self):
    pk = self.kwargs['pk']
    return Review.objects.filter(movielist=pk)
  
  
class ReviewCreate(generics.CreateAPIView):
  serializer_class = ReviewSerializer 
  
  def get_queryset(self):
    return Review.objects.all() 
  
  
  def perform_create(self,serializer):
    pk = self.kwargs.get('pk')
    movielist = MovieList.objects.get(pk=pk)
    
    review_user = self.request.user 
    review_queryset = Review.objects.filter(movielist=movielist,review_user=review_user)
    
    if review_queryset.exists():
      raise ValidationError("You have already posted Review")
    serializer.save(movielist= movielist, review_user=review_user)
    



class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Review.objects.all() 
  serializer_class = ReviewSerializer  


''' 

class ReviewDetail(mixins.ListModelMixin, 
                   mixins.UpdateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   generics.GenericAPIView): 
  queryset = Review.objects.all() 
  serializer_class = ReviewSerializer 
  
  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)



class ReviewList(mixins.ListModelMixin,
                   mixins.CreateModelMixin, 
                   mixins.DestroyModelMixin, 
                   generics.GenericAPIView): 
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer 
  
  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs) 
  
  def post(self, request, *args, **kwargs):
    
    return self.create(request, *args, **kwargs)
  
  def delete(self, request, *args, **kwargs): 
    return self.destroy(request, *args, **kwargs)
 '''

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