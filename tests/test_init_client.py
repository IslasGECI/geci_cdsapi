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
    island = "San Benito"
    obtained = construct_request(start_year, end_year, island)
    expected_year = [f"{start_year}", f"{end_year}"]
    assert obtained["year"] == expected_year
    assert obtained["month"][0] == "07"
    assert obtained["month"][-1] == "11"
    assert obtained["area"] == [32.35, -120.3, 24.25, -110.9]
    has_24_hours = len(obtained["time"]) == 24
    assert has_24_hours
    assert obtained["time"][0] == "00:00"
    has_all_days = len(obtained["day"]) == 31
    assert has_all_days
    assert obtained["day"][0] == "01"
    assert obtained["variable"] == ["10m_u_component_of_wind", "10m_v_component_of_wind"]


def test_load_access_key():
    obtained = load_access_key()
    assert obtained is not None
    assert len(obtained.split("-")) == 5


def test_init_client():
    obtained = init_client()
    expected_url = "https://cds.climate.copernicus.eu/api"
    assert obtained.url == expected_url
