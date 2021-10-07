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
    path('platform/',StreamPlatFormList.as_view(),name="platform"),
    path('<int:pk>/',WatchListDetailView.as_view(), name="movie_detail"),
    path('<int:pk>/review/',ReviewList.as_view(), name="review_list"),
    path('<int:pk>/review-create/',ReviewCreate.as_view(), name='review_create'),
    path('review/<int:pk>/',ReviewDetail.as_view(), name='review_list'),
   
]
