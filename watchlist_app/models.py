from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.      

class StreamPlatForm(models.Model): 
  name = models.CharField(max_length=30)
  about = models.CharField(max_length=150)
  website = models.URLField(max_length=100)
  
  def __str__(self):
    return self.name


class MovieList(models.Model):
  title = models.CharField(max_length=50)
  storyline = models.CharField(max_length=200)
  platform = models.ForeignKey(StreamPlatForm,on_delete=models.CASCADE,related_name="movielist")
  active   = models.BooleanField(default=True) 
  created  = models.DateTimeField(auto_now_add=True)
  objects = models.Manager()
  
  
  def __str__(self):
    return self.title
  



  
class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True) 
    movielist = models.ForeignKey(MovieList,on_delete=models.CASCADE,related_name="reviews")
    active = models.BooleanField(default=True) 
    created = models.DateTimeField(auto_now_add=True) 
    update = models.DateTimeField(auto_now=True)
    
    
    