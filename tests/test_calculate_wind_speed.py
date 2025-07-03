from geci_cdsapi.calculate_wind_speed import (
    calculate_monthly_wind_speed,
    calculate_wind_speed,
    mean_by_month,
    read_and_calculate_wind_speed,
    write_windspeed_dataset_to_csv,
)

import geci_test_tools as gtt
import xarray as xr
import numpy as np
import pandas as pd

nc_dataset = xr.open_dataset("tests/data/era5_wind_sanbenito_2013.nc")


def tests_read_and_calculate_wind_speed():
    directory_path = "tests/data"
    years = [2013, 2014]
    island = "San Benito"
    obtained = read_and_calculate_wind_speed(years, island, directory_path)
    expected_shape = (10,)
    assert obtained.wind_speed.shape == expected_shape


dataset_monthly_wind_speed = xr.Dataset(
    {
        "u10": (
            ("valid_time"),
            np.array([1, 2, 3]),
        ),
        "v10": (
            ("valid_time"),
            np.array([4, 5, 6]),
        ),
        "wind_speed": (
            ("valid_time"),
            np.array([7, 8, 9]),
        ),
    },
    coords={
        "valid_time": np.array(["2023-01-31", "2023-02-28", "2024-01-31"], dtype="datetime64[ns]"),
    },
)


def test_write_windspeed_dataset_to_csv():
    output_path = "tests/data/monthly_wind_speed.csv"
    write_windspeed_dataset_to_csv(dataset_monthly_wind_speed, output_path)
    gtt.assert_exist(output_path)
    obtained = pd.read_csv(output_path)
    expected_rows = 9
    assert len(obtained) == expected_rows
    expected_columns = ["Índice", "Año", "Mes/Periodo", "Valor"]
    assert obtained.columns == expected_columns
    assert obtained["Mes/Periodo"][0] == "Jan"


def test_calculate_monthly_wind_speed():
    obtained = calculate_monthly_wind_speed(nc_dataset)
    assert set(["u10", "v10", "wind_speed"]) == set(list(obtained.keys()))
    expected_shape = (5,)
    assert obtained.wind_speed.shape == expected_shape


dataset = xr.Dataset(
    {
        "u10": (
            ("valid_time", "latitude", "longitude"),
            np.array(
                [
                    [[1, 2, 3, 4], [5, 6, 7, 8]],
                    [[10, 20, 30, 40], [50, 60, 70, 80]],
                    [[1, 2, 3, 4], [5, 6, 7, 8]],
                ]
            ),
        ),
        "v10": (
            ("valid_time", "latitude", "longitude"),
            np.array(
                [
                    [[5, 6, 7, 8], [1, 2, 3, 4]],
                    [[1, 2, 3, 4], [5, 6, 7, 8]],
                    [[10, 20, 30, 40], [50, 60, 70, 80]],
                ]
            ),
        ),
    },
    coords={
        "valid_time": np.array(["2023-01-01", "2023-01-02", "2024-01-03"], dtype="datetime64[ns]"),
        "latitude": [10, 20],
        "longitude": [30, 40, 50, 60],
    },
)


def test_calculate_wind_speed():
    obtained = calculate_wind_speed(dataset)
    obtained_wind_speed_first_day_and_position = obtained[0, 0, 0].values
    assert np.sqrt(1**2 + 5**2) == obtained_wind_speed_first_day_and_position


def test_mean_by_month():
    obtained = mean_by_month(dataset)
    expected_shape = (13,)
    assert obtained.u10.shape == expected_shape
