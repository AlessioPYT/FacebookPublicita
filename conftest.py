from driver_manager import Driver
import pytest
from driver_manager import Appium
from driver_manager import DriverAppium
import subprocess
import logging
from appium.options.android import UiAutomator2Options
from XPATH_info import *

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='test_log.log')

def is_device_connected():
    try:
        result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
        if "device" in result.stdout.split():
            return True
    except Exception as e:
        logging.error(f"Error checking devices: {e}")
    return False

adb_output = subprocess.getoutput('adb devices')
if not adb_output or len(adb_output.splitlines()) == 1:
    raise EnvironmentError('No Android device found')
else:
    udid = adb_output.splitlines()[1].split()[0]

def get_driver_options() -> UiAutomator2Options:
    options = UiAutomator2Options()
    options.platform_name = platform_name
    options.platform_version = platform_version
    options.device_name = device_name
    options.app_package = app_package
    options.app_activity = app_activity
    options.no_reset = True
    options.udid = udid
    options.clear_device_logs_on_start = True
    options.auto_grant_permissions = True
    options.disable_window_animation = True
    return options


@pytest.fixture(scope="function", autouse=False)
def driver():
    if is_device_connected():
        logging.info("Device connected. Using Appium conn!")
        Appium.start()
        DriverAppium.start(get_driver_options)
        yield
        DriverAppium.finish()
        Appium.stop()
    else:
        logging.info("Device NON connected. Using Driver web brawser")
        Driver.start()
        workingWeb = Driver.open_browser()
        yield workingWeb
        Driver.finish()

