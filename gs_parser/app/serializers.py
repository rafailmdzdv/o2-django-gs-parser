from rest_framework import serializers

from app import models


class GasStationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.GasStation
        fields = ('latitude', 'longitude')


class DieselFuelTypesSerializer(serializers.ModelSerializer):

    gas_station = GasStationSerializer(read_only=True)

    class Meta:
        model = models.DieselFuelTypes
        fields = ('gas_station', 'df_price', 'df_taneko_price',
                  'df_winter_price', 'df_arctica_price')
