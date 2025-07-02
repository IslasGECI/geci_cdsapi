import os


def load_access_key():
    return os.environ.get("CDSAPI_KEY")
