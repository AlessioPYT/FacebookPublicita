
from appium.options.android import UiAutomator2Options
from appium.webdriver import Remote
from appium.webdriver.appium_connection import AppiumConnection
from selenium.common.exceptions import WebDriverException
from contextlib import suppress
from appium_manager import Appium

class Driver:
    app_package = 'com.facebook.katana'
    appium_instance = None

    @classmethod
    def start(cls, options: UiAutomator2Options) -> None:
        cls.appium_instance = Remote(AppiumConnection(f'{Appium.HOST}:{Appium.PORT}'), options=options)

    @classmethod
    def finish(cls) -> None:
        cls.appium_instance.terminate_app(cls.app_package)
        cls.appium_instance.quit()
        cls.appium_instance = None

    @classmethod
    def launch_app(cls) -> None:
        cls.appium_instance.activate_app(cls.app_package)

    @classmethod
    def terminate_app(cls) -> None:
        with suppress(WebDriverException):
            cls.appium_instance.terminate_app(cls.app_package)

