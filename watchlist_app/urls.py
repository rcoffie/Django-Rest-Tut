from django.urls import path
from . import views 

app_name = "watchlist_app"

urlpatterns = [
    path('',views.Movie_List,name="movie_list"),
    path('<int:pk>/',views.Movie_Detail,name="movie_detail"),
]
