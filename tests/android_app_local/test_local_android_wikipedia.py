from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
from selene import by


def test_local_android(mobile_management_android):
    with step('skip steps welcome screen'):
        browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/secondaryTextView")).should(
            have.texts("We’ve found the following on your device:"))
        browser.element(by.xpath("//android.widget.LinearLayout[2]")).click()
        browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(have.texts('New ways to explore'))
        browser.element(by.xpath("//android.widget.LinearLayout[3]")).click()
        browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(
            have.texts('Reading lists with sync'))
        browser.element(by.xpath("//android.widget.LinearLayout[4]")).click()
        browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(have.texts('Data & Privacy'))
        browser.element((AppiumBy.CLASS_NAME, "android.widget.Button")).click()
