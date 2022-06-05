from rest_framework.permissions import BasePermission, SAFE_METHODS#1.basepermission 2.has_permission 3.return true or false
#custom permissions
class IsReadonly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return False

class IsGetOrPostOrPut(BasePermission):
    def has_permission(self, request, view):
        allowed_method = ['GET', 'POST', 'PUT']
        if request.method in allowed_method:   
            return True
        else:
            return False 

class RolePermission(BasePermission):
    def has_permission(self, request, view):
        status = request.user.is_superuser
        print(request.user)
        print(dir(request.user))#check user attributes
        if status == True:
            allowed_method = ['GET', 'POST','PUT', 'DELETE']
            if request.method in allowed_method:
                return True
            else:
                return False
        else:
            if request.method in SAFE_METHODS:
                return True
            return False
class SubUserPermission(BasePermission):
    def has_permission(self, request, view):
        status = request.user.is_authenticated
        print(request.user)
        if status == True:
            allowed_method = ['GET', 'POST','PUT']
            if request.method in allowed_method:
                return True
            else:
                return False
        else:
            if request.method in SAFE_METHODS:
                return True
            return False
