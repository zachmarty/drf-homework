from rest_framework.permissions import BasePermission


class IsUserOrStaff(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.user == request.user


class IsModer(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="moder").exists()
