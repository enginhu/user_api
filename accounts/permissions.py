from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow owners and superusers of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.username == request.user.username or request.user.is_superuser