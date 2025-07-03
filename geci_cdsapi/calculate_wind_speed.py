import numpy as np
import xarray as xr


def read_and_calculate_wind_speed(years, island, directory_path):
    for year in years:
        nc = xr.open_dataset(f"{directory_path}/{island}_wind_{year}.nc")
        return calculate_monthly_wind_speed(nc)


def calculate_monthly_wind_speed(nc):
    nc["wind_speed"] = calculate_wind_speed(nc)
    return mean_by_month(nc)


def calculate_wind_speed(dataset):
    return np.sqrt(dataset["u10"] ** 2 + dataset["v10"] ** 2)


def mean_by_month(dataset):
    spatial_mean = dataset.mean(dim=["latitude", "longitude"])
    return spatial_mean.resample(valid_time="ME").mean()
