from django_filters.rest_framework import FilterSet
from .models import Hotel,Room

class HotelFilter(FilterSet):
    class Meta:
        model = Hotel
        fields = {
            'country': ['exact'],
            'city': ['exact'],
            'hotel_stars': ['exact']
        }

class RoomFilter(FilterSet):
    class Meta:
        model = Room
        fields = {
            'room_type': ['exact'],
            'room_status': ['exact'],
            'room_price': ['gt', 'lt'],
            'all_inclusive': ['exact'],
        }