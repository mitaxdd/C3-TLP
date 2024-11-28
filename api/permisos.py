from rest_framework import permissions

#gestion de permisos para limitar uso de ciertas funciones del crud, permitiendo solo q administrador academico y docente puedan hacer uso de ellas
class IsAdminOrReadOnly(permissions.BasePermission):


    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True
        print(request.user.groups)

        return request.user and request.user.groups.filter(name__in=['Administradoracademico', 'Docente']).exists()