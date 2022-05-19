from adb_cloud import get_oasis_credentials


def test_get_oasis_credentials() -> None:
    new_creds = get_oasis_credentials()
    assert new_creds.keys() == {
        "url",
        "hostname",
        "port",
        "dbName",
        "username",
        "password",
    }
    cached_creds = get_oasis_credentials()
    assert cached_creds == new_creds
