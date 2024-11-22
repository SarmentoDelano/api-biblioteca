from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsColecionador(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        return obj.colecionador == request.user
