from rest_framework import permissions

class ComentPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user.is_authenticated and request.user == obj.author)
