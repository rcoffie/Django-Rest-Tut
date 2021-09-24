from rest_framework import serializers  
from watchlist_app.models import *


class MovieSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  name = serializers.CharField(max_length=100)
  description = serializers.CharField(max_length=255) 
  active      = serializers.BooleanField()
  
  
  
  def create(self, validated_data):
    return Movie.objects.create(**validated_data)
  
  
  