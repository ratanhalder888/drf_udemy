from django.urls import path, include
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatDetailformAV
# from watchlist_app.api.views import movie_list, movie_details

urlpatterns = [
    # path('list/',movie_list, name='movie-list'),
    # path('<int:pk>/',movie_details, name='movie_details'),
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('list/<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),
    path('stream/', StreamPlatformAV.as_view(), name='stream-platform'),
    path('stream/<int:pk>/', StreamPlatDetailformAV.as_view(), name='streamplatform-detail'),

]