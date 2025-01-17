from selenium import webdriver

def initialize_driver():
    """Initializes and returns a Selenium WebDriver instance."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver