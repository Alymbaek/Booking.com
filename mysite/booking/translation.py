from .models import Hotel, Room
from modeltranslation.translator import TranslationOptions,register

@register(Hotel)
class HotelTranslationOptions(TranslationOptions):
    fields = ('hotel_name', 'country', 'city', 'address',  'hotel_description')

@register(Room)
class HotelTranslationOptions(TranslationOptions):
    fields = ('room_description',)