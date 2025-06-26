from geci_cdsapi import read_nc_file


def test_nc_file():
    nc_path = "tests/data/era5_wind_sanbenito_2013.nc"
    obtained = read_nc_file(nc_path)
    assert (["u10", "v10"] in obtained.keys()).all()
