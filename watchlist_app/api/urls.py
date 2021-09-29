from django.urls import path
from .views import  *
# from watchlist_app.views import MovieList,MovieDetailView

app_name = "watchlist_app"

""" urlpatterns = [
    path('',views.Movie_List,name="movie_list"),
    path('<int:pk>/',views.Movie_Detail,name="movie_detail"),
]
 """
 
urlpatterns = [
    path('',WatchList.as_view(), name="movie_list"),
    path('<int:pk>/',WatchListDetailView.as_view(), name="movie_detail"),
]
