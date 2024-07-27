from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from appium import webdriver as appium_webdriver
from appium.webdriver.appium_service import AppiumService
from appium.options.android import UiAutomator2Options
from contextlib import suppress
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
        options.add_argument("user-data-dir=C:\\Users\\Алексей\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1") # свой профиль
        cls.driver = webdriver.Chrome(options=options)
        return cls.driver
    
    @classmethod
    def open_browser(cls):
        logging.info("Opening browser from driver")
        cls.driver.get("https://www.facebook.com/")
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
    """
    1. Параметры -a и -p указывают IP-адрес и порт для запуска Appium. 
    Если они не указаны, Appium может использовать свои стандартные значения (например, 0.0.0.0 для IP и 4723 для порта).
    2. Параметры --relaxed-security и --allow-insecure отключают определенные уровни безопасности и разрешают небезопасные команды. 
    Без этих параметров, Appium может требовать более строгих условий безопасности.
    3. Параметр --allow-insecure с adb_shell позволяет Appium выполнять команды ADB через shell. 
    Если вы уберете этот параметр, могут возникнуть проблемы с выполнением определенных команд, требующих доступа через shell.
    """


    @classmethod
    def stop(cls) -> None:
        cls.service.stop()

class DriverAppium:
    app_package = 'com.facebook.katana'
    appium_instance = None

    @classmethod
    def start(cls, options: UiAutomator2Options) -> None:
        cls.appium_instance = appium_webdriver.Remote(
            command_executor=f'http://{Appium.HOST}:{Appium.PORT}/wd/hub',
            options=options
        )

    @classmethod
    def finish(cls) -> None:
        if cls.appium_instance:
            cls.appium_instance.quit()
            cls.appium_instance = None

    @classmethod
    def launch_app(cls) -> None:
        if cls.appium_instance:
            cls.appium_instance.activate_app(cls.app_package)

    @classmethod
    def terminate_app(cls) -> None:   # предназначен для завершения работы приложения на устройстве через Appium.
        if cls.appium_instance:
            with suppress(WebDriverException):
                cls.appium_instance.terminate_app(cls.app_package)

    @classmethod
    def grant_application_permissions(cls) -> None:
        if cls.appium_instance:
            permissions = [
                'ACCESS_FINE_LOCATION', 'ACCESS_COARSE_LOCATION', 'READ_EXTERNAL_STORAGE',
                'WRITE_EXTERNAL_STORAGE', 'CAMERA', 'READ_CONTACTS'
            ]
            platform_version = cls.appium_instance.capabilities.get('platformVersion', '0')

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


"""
1. ACCESS_FINE_LOCATION:
Описание: Позволяет приложению получать точное местоположение устройства с использованием GPS и сетевых источников (Wi-Fi, мобильные сети).
Использование: Приложения, которые требуют высокой точности местоположения, например, навигационные приложения.ACCESS_FINE_LOCATION:
Описание: Позволяет приложению получать точное местоположение устройства с использованием GPS и сетевых источников (Wi-Fi, мобильные сети).
Использование: Приложения, которые требуют высокой точности местоположения, например, навигационные приложения.

2. ACCESS_COARSE_LOCATION:
Описание: Позволяет приложению получать приблизительное местоположение устройства на основе сетевых источников (Wi-Fi, мобильные сети), 
без использования GPS.
Использование: Подходит для приложений, которые нуждаются в грубой оценке местоположения, например, для определения местоположения 
на карте в пределах города.

3. READ_EXTERNAL_STORAGE:
Описание: Позволяет приложению читать данные с внешнего хранилища (например, SD-карты).
Использование: Необходимо для приложений, которые работают с файлами, сохраненными на внешнем хранилище устройства, например, 
фотогалереи или файловых менеджеров.

4. WRITE_EXTERNAL_STORAGE:
Описание: Позволяет приложению записывать данные на внешнее хранилище.
Использование: Приложения, которые создают или изменяют файлы на внешнем хранилище, 
такие как загрузчики файлов или приложения для редактирования изображений.

5. CAMERA:
Описание: Позволяет приложению использовать камеру устройства для захвата изображений и видео.
Использование: Приложения для создания фотографий и видео, сканеры QR-кодов и другие функции, связанные с использованием камеры.

6. READ_CONTACTS:
Описание: Позволяет приложению считывать данные из списка контактов пользователя.
Использование: Приложения, которые синхронизируют, отображают или взаимодействуют с контактами пользователя, 
такие как приложения для обмена сообщениями или социальные сети.
"""