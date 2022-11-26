from rest_framework import permissions

class BlogPermission(permissions.BasePermission):
    def has_permisstion(self, request, view):
        if request.method in SAFT_METHODS:
            return True
        else:
            return bool(request.user.is_authenticated)

