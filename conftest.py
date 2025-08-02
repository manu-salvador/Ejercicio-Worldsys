import pytest
from pages.import_api import ImportAPI

@pytest.fixture(scope="session")
def api():
    token = "xxx"  # seteo el valor del token aca
    return ImportAPI(token)