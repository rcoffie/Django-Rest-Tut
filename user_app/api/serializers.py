from django.contrib.auth.models import User 
from rest_framework import serializers 



class RegistrationSerializer(serializers.ModelSerializer):
  password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
  
  class Meta:
    model = User 
    fields = ['username','email','password','password2']
    extra_kwargs = {
      'password' : {'write_only':True}
    }
    
  
  def save(self): 
    
    password = self.validated_data['password']
    password2 = self.validated_data['password2']
    
    if password != password2:
      raise serializers.ValidationError({'password and password2 must match'})
    
    if User.objects.filter(email=self.validated_data['email']).exists():
      raise serializers.ValidationError({'Email already Exists'}) 
    
    account = User(email=self.validate_data['email'],username=self.validate_data['username'])
    account.set_password(password)
    account.save()