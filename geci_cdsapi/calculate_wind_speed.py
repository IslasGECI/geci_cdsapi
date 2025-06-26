import xarray as xr


def read_nc_file(nc_path):
    nc = xr.open_dataset(nc_path)
    return nc
