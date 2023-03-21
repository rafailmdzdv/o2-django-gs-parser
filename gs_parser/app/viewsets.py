from rest_framework import viewsets

from app import models, serializers


class DieselFuelTypesViewset(viewsets.ModelViewSet):

    queryset = models.DieselFuelTypes.objects.all()
    serializer_class = serializers.DieselFuelTypesSerializer
