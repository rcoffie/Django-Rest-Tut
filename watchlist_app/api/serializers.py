from rest_framework import serializers  
from watchlist_app.models import *



class WatchListSerializer(serializers.ModelSerializer):
  
  class Meta:
    models = WatchList 
    fields = '__all__'
    
    
    

class StreamPlatFormSerializer(serializers.ModelSerializer):
  class Meta:
    model = StreamPlatForm 
    fields = '__all__'


''' def name_length(value):
  if len(value) < 2:
    raise serializers.ValidationError("Name is too short") '''
""" 
class MovieSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  name = serializers.CharField(validators=[name_length])
  description = serializers.CharField(max_length=255) 
  active      = serializers.BooleanField()
  
  
  
  def create(self, validated_data):
    return Movie.objects.create(**validated_data)
  
  def update(self, instance, validated_data): 
    instance.name = validated_data.get('name', instance.name)
    instance.description = validated_data.get('description', instance.description)
    instance.active = validated_data.get('active', instance.active)
    instance.save() 
    return instance
   """
''' class MovieSerializer(serializers.ModelSerializer):
  len_name = serializers.SerializerMethodField()
  
  class Meta:
    model = Movie 
    fields = "__all__"
  
  def get_len_name(self, object):
    length = len(object.name)
    return length
    
  def validate_name(self, value): 
    if len(value) < 3:
      raise serializers.ValidationError("Name is too short please")
    else: 
      return value 
    
  def validate(self, data): 
    if data['name'] == data['description']:
      raise serializers.ValidationError("Title and Description should be the same ")
    else:
      return data 
     '''
  
  
      
  
  
  