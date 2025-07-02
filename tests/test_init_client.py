from geci_cdsapi.init_client import (
    load_access_key,
    init_client,
    download_wind_netcdf_by_year,
    construct_request,
)
import geci_test_tools as gtt

import os
import pytest


@pytest.mark.skipif(os.getenv("GITHUB_ACTIONS") is None, reason="Solo se ejecuta en GitHub Actions")
def test_download_wind_netcdf_by_year():
    output_path = "tests/wind_2013.nc"
    download_wind_netcdf_by_year(2013, output_path)
    gtt.assert_exist(output_path)
    gtt.if_exist_remove(output_path)


def test_construct_request():
    start_year = 2014
    end_year = 2015
    obtained = construct_request(start_year, end_year)
    expected_year = [f"{start_year}", f"{end_year}"]
    assert obtained["year"] == expected_year


def test_load_access_key():
    obtained = load_access_key()
    assert obtained is not None
    assert len(obtained.split("-")) == 5


def test_init_client():
    obtained = init_client()
    expected_url = "https://cds.climate.copernicus.eu/api"
    assert obtained.url == expected_url
