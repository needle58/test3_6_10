import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_btn_add_cart(browser):
    browser.get(link)
    time.sleep(30)
    buttons = browser.find_elements(By.CLASS_NAME,'btn-add-to-basket')
    assert len(buttons) > 0, 'button not find'
