import pytest
from driver_manager import Driver
from appium_manager import Appium
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope='session')
def appium_service():
    Appium.start()
    yield
    Appium.stop()

@pytest.fixture(scope='session', autouse=True)
def driver(appium_service):
    options = UiAutomator2Options()
    Driver.start(options)
    Driver.launch_app()
    yield
    Driver.finish()