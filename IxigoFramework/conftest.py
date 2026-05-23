import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.env import ConfigReader
import undetected_chromedriver as uc

@pytest.fixture(scope="session")
def setup_and_teardown():

    # Reading the config
    config = ConfigReader.read_config()
    env = config["qa"]
    base_url = env["base_url"]

    options = uc.ChromeOptions()

    options.add_argument("--disable-notifications")

    prefs = {
        "profile.default_content_setting_values.notifications": 2
    }

    options.add_experimental_option("prefs", prefs)

    # Setup
    driver = uc.Chrome(
        options=options,
        version_main=140
    )

    driver.maximize_window()
    driver.get(base_url)

    yield driver

    # Teardown
    driver.quit()