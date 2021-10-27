from django.urls import path
from user_app.api.views import  *
from rest_framework.authtoken.views import obtain_auth_token

 
urlpatterns = [
   path('login', obtain_auth_token,name='login'),
   path('registration/',registration_view, name="registration")
]
