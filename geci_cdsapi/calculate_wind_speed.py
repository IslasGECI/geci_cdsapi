import xarray as xr
import numpy as np


def read_nc_file(nc_path):
    nc = xr.open_dataset(nc_path)
    nc["wind_speed"] = np.sqrt(nc["u10"] ** 2 + nc["v10"] ** 2)
    return nc
