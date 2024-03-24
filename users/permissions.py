from rest_framework import permissions 

class IsObjectOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return obj.user == request.user 
        
        return obj.user == request.user 
    