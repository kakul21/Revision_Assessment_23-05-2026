import pytest
from Pages.Ixigo_page import Ixigo
from config.env import ConfigReader
from time import sleep
from utils.loggers import get_logger

@pytest.mark.smoke
def test_book_ticket(setup_and_teardown):

    driver = setup_and_teardown
    ixigo_page = Ixigo(driver)

    config = ConfigReader.read_config()
    env = config["qa"]
    BASE_URL = env['base_url']
    EMAIL = env['email']
    PASSWORD = env['password']
    driver.get(BASE_URL)

    # get_logger().info("Trying to Log In")
    sleep(5)
    ixigo_page.close_popup()
    ixigo_page.click_login()
    sleep(5)

    ixigo_page.switch_to_google_iframe()
    ixigo_page.click_google_signin()
    sleep(3)

    # return to main DOM
    driver.switch_to.default_content()

    # switch to new google popup window
    ixigo_page.switch_to_google_window()

    # enter email
    ixigo_page.enter_google_email(EMAIL)
    ixigo_page.click_email_next()
    sleep(3)

    # enter password
    ixigo_page.enter_google_password(PASSWORD)
    ixigo_page.click_password_next()
    sleep(5)

    # ixigo_page.click_continue()

    # switch back to main window
    driver.switch_to.window(ixigo_page.main_window)

    get_logger().info("Login Successful")




