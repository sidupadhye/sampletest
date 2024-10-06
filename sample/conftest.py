import pytest

@pytest.fixture(autouse=True, scope="package")
def setup_and_teardown():
    print("Launch Browser")
    print("Open Appication URL in Browser")
    yield
    print("Logout from Application")
    print("Close Browser")