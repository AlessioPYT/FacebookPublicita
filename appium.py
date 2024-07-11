from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.appium_service import AppiumService
from contextlib import suppress
from appium.options.android import UiAutomator2Options
from appium.webdriver import Remote
from appium.webdriver.appium_connection import AppiumConnection
from selenium.common.exceptions import WebDriverException

#  "C:\Users\Алексей\AppData\Local\Programs\Python\Python312\python.exe" "C:\Users\Алексей\Desktop\python_work\FaceBookPublicita\test.appium.py"


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

class Driver:
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

# Настройка опций для UiAutomator2
options = UiAutomator2Options()
options.platform_name = "Android"
options.platform_version = "11.0"
options.device_name = "R9HR6027NSD"
options.app_package = "com.facebook.katana"
options.app_activity = "com.facebook.katana.LoginActivity"

# Запуск сервиса Appium
Appium.start()

# Запуск драйвера
Driver.start(options)

try:
    # Используем WebDriverWait для ожидания видимости элемента
    email_field = WebDriverWait(Driver.appium_instance, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="screenshotContainer"]/div[2]/div/div/div/div/div[81]'))
    )
    # //*[@id="screenshotContainer"]/div[2]/div/div/div/div/div[112] //*[@id="screenshotContainer"]/div[2]/div/div/div/div/div[113]
    email_field.click()

    password_field = WebDriverWait(Driver.appium_instance, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="screenshotContainer"]/div[2]/div/div/div/div/div[60]'))
    )
    password_field.click()

finally:
    # Закрытие драйвера и остановка сервиса
    Driver.finish()
    Appium.stop()
