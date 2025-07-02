import cdsapi
import os


def download_wind_netcdf_by_year(year, output_path):
    client = init_client()
    dataset = "reanalysis-era5-single-levels"
    request_params = construct_request(year)
    client.retrieve(dataset, request_params, output_path)


def construct_request(start_year, end_year):
    years = [str(year) for year in range(start_year, end_year + 1)]
    request_params = {
        "product_type": "reanalysis",
        "variable": ["10m_u_component_of_wind"],
        "year": years,
        "month": ["07", "08", "09", "10", "11"],
        "day": ["01"],
        "time": ["00:00"],
        "format": "netcdf",
        "area": [32, -120, 31.5, -119.5],
    }
    return request_params


def init_client():
    client = cdsapi.Client(url="https://cds.climate.copernicus.eu/api", key=load_access_key())
    return client


def load_access_key():
    return os.environ.get("CDSAPI_KEY")
