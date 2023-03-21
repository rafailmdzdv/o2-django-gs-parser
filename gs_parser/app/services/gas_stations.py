import numpy as np
import pandas as pd
import xlrd

from app import models
from app.utils import price
from gs_parser import settings


def parse_gas_stations_xls() -> None:
    workbook = _get_workbook()
    for _, row in workbook.iterrows():
        gas_station = _add_or_get_gs_model(row)
        _add_or_update_fuel_model(gas_station, row)


def _get_workbook() -> pd.DataFrame:
    workbook = xlrd.open_workbook(settings.XLS_PATH,
                                  ignore_workbook_corruption=True)
    pd_workbook = pd.read_excel(workbook).replace(np.nan, None)
    return pd_workbook


def _add_or_get_gs_model(row: pd.Series) -> models.GasStation:
    gas_station, _ = models.GasStation.objects.get_or_create(
        latitude=row['Координаты GPS (широта)'],
        longitude=row['Координаты GPS (долгота)']
    )
    return gas_station


def _add_or_update_fuel_model(gas_station: models.GasStation,
                              row: pd.Series) -> None:
    fuels = map(price.to_float, [row['ДТ'], row['ДТ ТАНЕКО'],
                                 row['ДТ (зимнее)'], row['ДТ Арктика']])
    df_price, df_taneko_price, df_winter_price, df_arctica_price = fuels
    fuel, created = models.DieselFuelTypes.objects.get_or_create(
        gas_station=gas_station,
        defaults={
            'df_price': df_price,
            'df_taneko_price': df_taneko_price,
            'df_winter_price': df_winter_price,
            'df_arctica_price': df_arctica_price
        }
    )
    if not created:
        fuel.df_price = df_price
        fuel.df_taneko_price = df_taneko_price
        fuel.df_winter_price = df_winter_price
        fuel.df_arctica_price = df_arctica_price
        fuel.save()
