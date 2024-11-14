from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
class UserProfile(AbstractUser):
    ROLE_CHOICES = [
        ('SimpleUser', 'SimpleUser'),
        ('ownerUser', 'ownerUser'),
    ]
    user_role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='SimpleUser')
    phone_number = PhoneNumberField(default='KG', null=True, blank=True)
    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True,
                                           validators=[MinValueValidator(18), MaxValueValidator(100)])

    def __str__(self):
        return self.username


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel_description = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    address = models.CharField(max_length=32)
    hotel_stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='Рейтинг', null=True,
                                blank=True)
    hotel_video = models.FileField(upload_to='hotel_video/', null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.hotel_name}'

    def get_average_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            return round(sum(review.stars for review in reviews) / reviews.count(), 1)
        return 0


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_images')
    hotel_image = models.ImageField(upload_to='hotel_image/')


class Room(models.Model):
    room_number = models.PositiveSmallIntegerField()
    hotel_room = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_rooms')
    TYPE_CHOICES = [
        ('люкс', 'люкс'),
        ('семейный', 'семейный'),
        ('одноместный', 'одноместный'),
        ('двухместный', 'двухместный'),

    ]
    room_type = models.CharField(max_length=16, choices=TYPE_CHOICES)
    STATUS_CHOICES = [
        ('свободен', 'свободен'),
        ('забронирован', 'забронирован'),
        ('занят', 'занят'),
    ]
    room_status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='свободен')
    room_price = models.PositiveIntegerField()
    all_inclusive = models.BooleanField(default=False)
    room_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.hotel_room} - {self.room_number} - {self.room_type}'

class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_image')
    room_image = models.ImageField(upload_to='room_image/')


class Review(models.Model):
    user_name = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, related_name='reviews', on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='Рейтинг', null=True,
                                blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.user_name} - {self.hotel} - {self.stars}'


class Booking(models.Model):
    hotel_booking = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_booking = models.ForeignKey(Room, on_delete=models.CASCADE)
    user_booking = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    total_price = models.PositiveIntegerField(default=0)
    STATUS_BOOK_CHOICES = [
        ('отменено', 'отменено'),
        ('подтверждено', 'подтверждено'),
    ]
    status_book = models.CharField(max_length=16, choices=STATUS_BOOK_CHOICES)
    date_booking = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user_booking} - {self.hotel_booking} - {self.room_booking} - {self.status_book}'

    def save(self, *args, **kwargs):
        if self.room_booking.room_status == 'занят':
            raise ValueError("Зто комната Занят")
        if self.room_booking.room_status == 'забронирован':
            raise ValueError("Зто комната Забронирован")
        else:
            self.room_booking.room_status = 'забронирован'

            self.room_booking.save()
        super().save(*args, **kwargs)







