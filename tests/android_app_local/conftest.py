import allure
import pytest
import allure_commons
from appium.options.android import UiAutomator2Options
from selene import browser

import config
from appium import webdriver


@pytest.fixture(scope='function')
def mobile_management_android():
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        # Параметры PlatformName automationName указаны по дефолту в экземпляре класса UiAutomator2Options()
        "udid": "emulator-5554",
        "app": r"C:\Users\user\Downloads\app-alpha-universal-release (1).apk",
        "appPackage": "org.wikipedia.alpha",
        "appActivity": "org.wikipedia.main.MainActivity"
    })

    browser.config.timeout = config.config.timeout
    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            'http://127.0.0.1:4723',
            options=options
        )

    browser.config.wait_decorator = allure_commons._allure.step
    yield

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

    #session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

    #utils_allure.attach_bstack_video(session_id, version_driver="app-")

    browser.quit()
