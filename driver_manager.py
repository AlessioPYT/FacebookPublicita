from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from appium.webdriver.appium_service import AppiumService
from contextlib import suppress
from appium.options.android import UiAutomator2Options
from appium.webdriver import Remote
from appium.webdriver.appium_connection import AppiumConnection
from selenium.common.exceptions import WebDriverException
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='test_log.log')

class Driver():
    driver = None

    @classmethod
    def start(cls):
        logging.info("Start Browser")
        options = Options()
        options.add_argument("dom.webnotifications.enabled")
        prefs = {"profile.default_content_setting_values.notifications": 2}  # Отключить уведомления
        options.add_experimental_option("prefs", prefs)
        # chrome_options.add_argument("--headless")   # фоновий режим
        options.add_argument("user-data-dir=C:\\Users\\Алексей\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1") # свой профиль          
        cls.driver = webdriver.Chrome(options=options)
        return cls.driver
    
    @classmethod
    def open_browser(cls):
        logging.info("Opening browser from driver")
        cls.driver.get("https://www.facebook.com/")
        # WebDriverWait(cls.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))                        
        return cls.driver    
        
    @classmethod                                        
    def finish(cls):
        if cls.driver:
            logging.info("Close driver")
            cls.driver.quit()


class Appium:
    service = AppiumService()
    HOST = "127.0.0.1"
    PORT = "4723"

    @classmethod
    def start(cls) -> None:
        cls.service.start(
            args=['-a', cls.HOST, '-p', cls.PORT, '--relaxed-security', '--allow-insecure', 'adb_shell']
        )

    @classmethod
    def stop(cls) -> None:
        cls.service.stop()

class DriverAppium:
    app_package = 'com.facebook.katana'
    appium_instance = None

    @classmethod
    def start(cls, options: UiAutomator2Options) -> None:
        cls.appium_instance = Remote(AppiumConnection(f'http://{Appium.HOST}:{Appium.PORT}'), options=options)

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

    @classmethod
    def grant_application_permissions(cls) -> None:
        permissions = [
            'ACCESS_FINE_LOCATION', 'ACCESS_COARSE_LOCATION', 'READ_EXTERNAL_STORAGE',
            'WRITE_EXTERNAL_STORAGE', 'CAMERA', 'READ_CONTACTS'
        ]
        platform_version = cls.appium_instance.capabilities['platformVersion']

        if int(platform_version) >= 10:
            permissions.append('ACCESS_BACKGROUND_LOCATION')

        if int(platform_version) >= 13:
            permissions.append('POST_NOTIFICATIONS')

        for permission in permissions:
            with suppress(WebDriverException):
                cls.appium_instance.execute_script(
                    'mobile: shell',
                    {'command': 'pm grant', 'args': [f'{cls.app_package} android.permission.{permission}']}
                )  


