from django.urls import path, include
from rest_framework import routers

from app import viewsets


router = routers.DefaultRouter()
router.register('gas_stations', viewsets.DieselFuelTypesViewset)


urlpatterns = [
    path('', include(router.urls))
]
