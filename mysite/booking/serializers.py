from .models import *
from rest_framework import serializers


class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'age', 'password', 'phone_number']

class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']

class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username']

class HotelSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['hotel_name']

class RoomSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['room_number']

class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['id','room', 'room_image']

class RoomImageSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['room_image']


class RoomListSerializer(serializers.ModelSerializer):
    room_image = RoomImageSimpleSerializer(read_only=True, many=True)

    class Meta:
        model = Room
        fields = ['id', 'room_number', 'room_type', 'room_status', 'room_price',  'room_image', 'all_inclusive']

class RoomDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'room_number', 'room_type', 'room_status',
                  'all_inclusive', 'room_price', 'room_description']



class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['hotel', 'hotel_image']


class HotelImageSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['hotel_image']

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['id', 'hotel', 'text', 'stars', 'parent']





class HotelListSerializer(serializers.ModelSerializer):
    hotel_images = HotelImageSimpleSerializer(read_only=True, many=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = ['average_rating', 'hotel_name', 'country', 'city', 'hotel_images', 'hotel_stars', 'created_date']

    def get_average_rating(self, obj):
        return obj.get_average_rating()


class HotelDetailSerializer(serializers.ModelSerializer):
    hotel_images = HotelImageSimpleSerializer(read_only=True, many=True)
    reviews = ReviewSerializer(read_only=True, many=True)
    hotel_rooms = RoomListSerializer(read_only=True, many=True)
    owner = UserProfileSimpleSerializer()
    average_rating = serializers.SerializerMethodField()
    class Meta:
        model = Hotel
        fields = ['id', 'average_rating', 'hotel_name', 'country', 'city', 'address', 'hotel_stars', 'hotel_images', 'hotel_video',
                  'reviews', 'created_date', 'owner', 'hotel_rooms']


    def get_average_rating(self, obj):
        return obj.get_average_rating()

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'hotel_booking', 'room_booking', 'user_booking',
                  'check_in', 'check_out', 'status_book', 'total_price', 'date_booking']







