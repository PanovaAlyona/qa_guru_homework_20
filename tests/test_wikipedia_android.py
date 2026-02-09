from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


def test_search():

    with step('Онбординг на первой странице'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")
                        ).should(have.text("The Free Encyclopedia"))
        browser.element((AppiumBy.ID,
                         'org.wikipedia.alpha:id/fragment_onboarding_forward_button')
                        ).should(be.visible).click()


    with step('Онбординг на второй странице'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")
                        ).should(have.text('New ways to explore'))
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")
                        ).should(be.visible).click()

    with step('Онбординг на третьей странице'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
                        ).should(have.text('Reading lists with sync'))
        browser.element((AppiumBy.ID,
                         'org.wikipedia.alpha:id/fragment_onboarding_forward_button')
                        ).should(be.visible).click()

    with step('Онбординг на четвертой странице'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
                        ).should(have.text('Data & Privacy'))
        browser.element((AppiumBy.ID,
                         'org.wikipedia.alpha:id/fragment_onboarding_done_button')
                        ).should(be.visible).click()