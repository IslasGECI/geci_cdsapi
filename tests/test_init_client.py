from geci_cdsapi.init_client import load_access_key


def test_load_access_key():
    obtained = load_access_key()
    assert obtained is not None
