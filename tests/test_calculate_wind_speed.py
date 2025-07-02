from geci_cdsapi.calculate_wind_speed import calculate_wind_speed, read_nc_file, mean_by_month
import xarray as xr
import numpy as np


def test_nc_file():
    nc_path = "tests/data/era5_wind_sanbenito_2013.nc"
    obtained = read_nc_file(nc_path)
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
