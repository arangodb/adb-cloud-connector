from adb_cloud_connector import get_temp_credentials

def test_get_temp_credentials() -> None:
    new_creds = get_temp_credentials()
    print(new_creds)
    assert new_creds.keys() == {
        "url",
        "hostname",
        "port",
        "dbName",
        "username",
        "password",
    }
    cached_creds = get_temp_credentials()
    assert cached_creds == new_creds
test_get_temp_credentials()
    
