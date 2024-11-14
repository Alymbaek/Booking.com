from django.urls import path, include
from .views import *
from rest_framework import routers
router = routers.DefaultRouter()

router.register(r'hotels', HotelListViewSet, basename='hotel-list'),
router.register(r'hotels-detail', HotelDetailViewSet, basename='hotel-detail'),
router.register(r'users', UserProfileListViewSet, basename='users-list'),
router.register(r'users-detail', UserProfileDetailViewSet, basename='users-detail'),
router.register(r'rooms', RoomListViewSet, basename='rooms-list'),
router.register(r'rooms-detail', RoomDetailViewSet, basename='rooms-detail'),
router.register(r'reviews', ReviewViewSet, basename='review-list'),
router.register(r'reviews-detail', ReviewViewSet, basename='review-detail'),

router.register(r'booking', BookingViewSet, basename='booking-list'),
router.register(r'booking-detail', BookingViewSet, basename='booking-detail'),
router.register(r'room_image', RoomImageViewSet, basename='room-list'),
router.register(r'room_image-detail', RoomImageViewSet, basename='room-detail'),









urlpatterns = [
    path('', include(router.urls))
]