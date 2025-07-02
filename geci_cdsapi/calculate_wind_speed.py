import xarray as xr
import numpy as np


def read_nc_file(nc_path):
    nc = xr.open_dataset(nc_path)
    nc["wind_speed"] = calculate_wind_speed(nc)
    return mean_by_month(nc)


def calculate_wind_speed(dataset):
    return np.sqrt(dataset["u10"] ** 2 + dataset["v10"] ** 2)


def mean_by_month(dataset):
    spatial_mean = dataset.mean(dim=["latitude", "longitude"])
    return spatial_mean.resample(valid_time="ME").mean()
