from rest_framework import permissions

class Owner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'ownerUser':
            return False
        return True

class CrudOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.user_role == 'ownerUser'



class CheckHotelOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class CheckRoom(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.room_status == 'свободен':
            return True
        return False

class CheckBookingOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'SimpleUser':
            return True
        return False

class ReviewOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.user_name == request.user:
            return True
        return False


class RoomOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.hotel_room.owner == request.user:
            return True
        return False

class BookingOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.user_booking == request.user:
            return True
        return False


class RoomImagesOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.user_role == 'ownerUser'
