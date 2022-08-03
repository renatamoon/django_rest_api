# STANDARD IMPORTS
from rest_framework import permissions


class IsSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        # it will only have permission to delete if it's superuser
        if request.method == "DELETE":
            if request.user.is_superuser:
                return True
        return False
