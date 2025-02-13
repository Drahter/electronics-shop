from rest_framework import permissions


class IsActive(permissions.BasePermission):
    """
    Только те, кто создавал объекты, могут с ними взаимодействовать.
    """

    def has_is_active_status(self, request):
        return request.user.is_active is True
