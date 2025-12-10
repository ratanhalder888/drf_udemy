from django.urls import path, include
from watchlist_app.api.views import (WatchListAV, WatchDetailAV, StreamPlatformAV,
                                      StreamPlatformDetailAV, ReviewList, ReviewDetail,
                                      ReviewCreate, StreamPlatformVS, UserReview,
                                      WatchListGV)
# from watchlist_app.api.views import movie_list, movie_details
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'streamplatform', StreamPlatformVS, basename='streamplatform')


urlpatterns = [
    # path('list/',movie_list, name='movie-list'),
    # path('<int:pk>/',movie_details, name='movie_details'),
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),
    path('list2/', WatchListGV.as_view(), name='watch-list'),

    path('', include(router.urls)),

    # path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    # path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),

    
    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>/', ReviewDetail.as_view(), name='review_detail'),

    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review_detail'),

    # path('review/<str:username>/', UserReview.as_view(), name='user-review-details'),
    path('review/', UserReview.as_view(), name='user-review-details'),

]