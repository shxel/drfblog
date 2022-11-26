from rest_framework import permissions

class BlogPermisstion(permissions.BasePermission):
    def has_permisstion_view(self, request, view, obj):
        if request.method in permissions.SAFT_METHODS and obj.author == request.user:
            return True
        else:
            return request.user

