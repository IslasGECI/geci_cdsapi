from geci_cdsapi.init_client import load_access_key, init_client


def test_load_access_key():
    obtained = load_access_key()
    assert obtained is not None
    assert len(obtained.split("-")) == 5


def test_init_client():
    obtained = init_client()
    expected_url = "https://cds.climate.copernicus.eu/api"
    assert obtained.url == expected_url
