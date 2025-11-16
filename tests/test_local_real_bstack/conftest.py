import allure
import pytest
import allure_commons
from appium.options.android import UiAutomator2Options
from selene import browser
from config import config
from selene_in_action import utils
from selene_in_action.utils import allure as utils_allure
from appium import webdriver
#from allure_commons.types import AttachmentType
import dotenv


@pytest.fixture(scope='function')
def mobile_management():
    options = UiAutomator2Options()

    # Базовые capabilities
    options.set_capability('platformName', 'Android')
    options.set_capability('appActivity', 'org.wikipedia.main.MainActivity')
    options.set_capability('appPackage', 'org.wikipedia.alpha')

    if config.context in ['local_real', 'local_emulator']:
        options.set_capability('enableVideo', True)
        options.set_capability('videoQuality', 'medium')
        options.set_capability('videoScale', '1280x720')

    # Выбираем устройство в зависимости от контекста
    if config.context == 'local_emulator':
        options.set_capability('udid', dotenv.dotenv_values('.env.local_emulator').get('UDID'))  # Ваш id эмулятора
    elif config.context == 'local_real':
        options.set_capability('udid',
                               dotenv.dotenv_values('.env.local_real').get('UDID'))  # Ваш id реального устройства
    elif config.context == 'bstack':
        options.set_capability('deviceName', config.deviceName)
        options.set_capability('platformVersion', '13.0')

    # Устанавливаем app
    options.set_capability('app', (
        config.app if (config.app.startswith('/') or config.app.startswith('bs://'))
        else utils.file.abs_path_from_project(config.app)
    ))

    # BrowserStack специфичные настройки
    if config.context == 'bstack':
        bstack_options = {
            "projectName": config.BROWSERSTACK_PROJECT_NAME,
            "buildName": config.BROWSERSTACK_BUILD_NAME,
            "sessionName": config.BROWSERSTACK_SESSION_NAME,
            "userName": config.BROWSERSTACK_USERNAME,
            "accessKey": config.BROWSERSTACK_ACCESS_KEY,
        }
        options.set_capability('bstack:options', bstack_options)

    # Настройка браузера
    browser.config.timeout = config.timeout
    browser.config.wait_decorator = allure_commons._allure.step

    # Запуск драйвера
    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            config.remote_url,
            options=options
        )

    yield

    # Attachments после теста
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG,
    )

    allure.attach(
        browser.driver.page_source,
        name='screen xml dump',
        attachment_type=allure.attachment_type.XML,
    )

    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()
    # Прикрепляем видео для реального девайса или эмулятора
    # if config.context == 'local_real' or 'local_emulator':

    # video_url = config.remote_url + '/' + browser.driver.session_id + ".mp4"
    # html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
    #        + video_url \
    #        + "' type='video/mp4'></video></body></html>"
    # allure.attach(html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html')
    # Прикрепляем видео для BrowserStack
    if config.context == 'bstack':
        utils_allure.attach_bstack_video(session_id, version_driver="app-")
