from django.db import models


class GasStation(models.Model):
    latitude = models.CharField(max_length=30)
    longitude = models.CharField(max_length=30)


class DieselFuelTypes(models.Model):
    gas_station = models.ForeignKey(GasStation, on_delete=models.CASCADE)
    df_price = models.FloatField(blank=True)
    df_taneko_price = models.FloatField(blank=True)
    df_winter_price = models.FloatField(blank=True)
    df_arctica_price = models.FloatField(blank=True)
