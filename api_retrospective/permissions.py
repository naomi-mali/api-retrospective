from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only the owner
    of an object to edit or delete it.
    Read-only permissions are allowed for any request.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsSenderOrReceiver(permissions.BasePermission):
    """
    Custom permission to allow only the sender or receiver of an object
    to access or modify it.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.sender == request.user or obj.receiver == request.user


class IsChatSender(permissions.BasePermission):
    """
    Custom permission to allow only the sender of a chat to delete or edit it.
    Read-only permissions are allowed for any request.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.sender == request.user
