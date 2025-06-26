from geci_cdsapi.calculate_wind_speed import read_nc_file


def test_nc_file():
    nc_path = "tests/data/era5_wind_sanbenito_2013.nc"
    obtained = read_nc_file(nc_path)
    assert set(["u10", "v10"]) == set(list(obtained.keys()))
