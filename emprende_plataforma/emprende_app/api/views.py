from emprende_app.api.serializers import RolesSerializer
from emprende_app.models import Roles
from rest_framework import generics


#Para obtener una lista de los roles
class RolesLista(generics.ListAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer
    
#para crear los roles
class RolesCrear(generics.CreateAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer