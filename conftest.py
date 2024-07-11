from driver_manager import Driver
import pytest


@pytest.fixture(scope="function", autouse=True)
def driver():
    Driver.start()
    driver_instance = Driver.open_browser()
    yield driver_instance
    Driver.finish()