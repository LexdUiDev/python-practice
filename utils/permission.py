from rest_framework.permissions import BasePermission


class IsFemaleUser(BasePermission):
    def has_permission(self, request, view):
        user= request.user

        if user.gender!= 'female':
            return False
        return True