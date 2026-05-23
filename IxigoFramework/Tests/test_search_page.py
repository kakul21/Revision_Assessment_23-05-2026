import pytest
from Pages.search_page import SearchPage
from config.env import ConfigReader
from time import sleep

@pytest.mark.smoke
def test_search_flight(setup_and_teardown):

    driver = setup_and_teardown

    search_page = SearchPage(driver)

    # CONFIG
    config = ConfigReader.read_config()
    env = config["qa"]

    BASE_URL = env["base_url"]
    # FROM_CITY = env["from_city"]
    # TO_CITY = env["to_city"]

    # OPEN WEBSITE
    driver.get(BASE_URL)
    sleep(5)
    search_page.close_popup()
    search_page.from_destination()
    sleep(2)
    search_page.select_from_city()
    sleep(2)
    search_page.select_to_city()
    sleep(2)
    search_page.select_date()
    sleep(2)
    search_page.travellers_click()
    search_page.click_search()
    search_page.click_book()
    sleep(5)
    search_page.select_free_booking_cancellation()




